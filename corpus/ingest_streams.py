#!/usr/bin/env python3
"""Ingest material from OTHER SocrateAI streams (and this repo's own docs) that
QC Stream 1 builds on, into ANSE's Chroma store, collection `qc_streams`.

Pattern taken from SocrateAI-Scientific-CondensedMatterTheory
corpus/ingest_generated.py (worktree adscmt-litreview), extended to read files
from sibling repositories.

Kept apart from `qc_literature` on purpose. Everything here is SocrateAI
writing: AI-assisted and not peer reviewed. Every Lean result in it is
conditional on the unreviewed upstream theorem
`OAI.AtomicTriangular.universal_energy_minimum` (openai/math). A retrieval hit
must say so, so every record carries `provenance`, `source_kind`, `repo`,
`path`, `git_commit`, `sha256` and a `tier_note`.

Same embedder and fail-closed rule as ingest_chroma.py (ANSE's
OllamaEmbeddingFunction, qwen3-embedding:0.6b, 1024-d, no hash fallback).
Deterministic ids `stream::<repo>::<path>::<n>` with upsert; chunks of a file
whose sha256 changed or that left SOURCES are deleted.

    python3 corpus/ingest_streams.py --dry-run
    python3 corpus/ingest_streams.py
"""
from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ingest_chroma import (  # noqa: E402
    DEFAULT_CHROMA_PATH, chunk, clean, extract_pdf_text, load_anse_embedding_function,
)

HOME = Path.home()
ROOT = Path(__file__).resolve().parent.parent
COLLECTION = "qc_streams"

TUO = HOME / "triangular-universal-optimality-lean"
TUO_GUIDE = TUO / ".claude" / "worktrees" / "physics-skyrmion"
CONDITIONAL = ("Lean results conditional on unreviewed upstream openai/math "
               "universal_energy_minimum; statement fidelity (RED_TEAM T1) open")

# (repo_root, relative glob, source_kind, tier_note); first match wins per file.
SOURCES: list[tuple[Path, str, str, str]] = [
    (TUO, "README.md", "stream_readme", CONDITIONAL),
    (TUO, "LIMITATIONS.md", "stream_limitations", CONDITIONAL),
    (TUO, "LITERATURE.md", "stream_literature", "literature notes (Tier L pointers)"),
    (TUO, "METHODOLOGY.md", "stream_methodology", CONDITIONAL),
    (TUO, "RED_TEAM.md", "stream_red_team", CONDITIONAL),
    (TUO, "RED_TEAM_LOG.md", "stream_red_team", CONDITIONAL),
    (TUO, "PROVENANCE.md", "stream_provenance", "provenance record"),
    (TUO, "verification/statement_fidelity.md", "stream_audit", "AI-only statement-fidelity audit"),
    # The physicist guide (v0.3.0 guide.pdf) lives on the unmerged physics-skyrmion worktree branch.
    (TUO_GUIDE, "docs/physicist_guide/guide.tex", "stream_guide", CONDITIONAL + "; Yukawa Tier C"),
    (TUO, "prereg/*.json", "stream_prereg", "preregistration (hypothesis + kill criterion)"),
    (HOME, "triangular_uo_v0.*_notes.md", "release_notes", CONDITIONAL),
    # This repository's own planning documents.
    (ROOT, "docs/*.md", "qc_doc", "QC Stream 1 planning; Tier C unless stated"),
    (ROOT, "README.md", "qc_readme", "QC Stream 1 planning; Tier C unless stated"),
]


def git_commit(repo: Path) -> str:
    r = subprocess.run(["git", "-C", str(repo), "rev-parse", "--short", "HEAD"],
                       capture_output=True, text=True)
    return r.stdout.strip() or "untracked"


def tracked(repo: Path, path: Path) -> bool:
    if git_commit(repo) == "untracked":
        return True  # loose files (release notes in $HOME) are not in a repo
    r = subprocess.run(["git", "-C", str(repo), "ls-files", "--error-unmatch",
                        str(path.relative_to(repo))], capture_output=True)
    return r.returncode == 0


def collect() -> list[tuple[Path, Path, str, str]]:
    seen, out = set(), []
    for repo, pattern, kind, tier in SOURCES:
        for p in sorted(repo.glob(pattern)):
            if p in seen or not p.is_file() or ".claude" in p.relative_to(repo).parts:
                continue
            if not tracked(repo, p):
                continue  # a retrieval hit must be reproducible from git
            seen.add(p)
            out.append((repo, p, kind, tier))
    return out


def text_of(p: Path) -> str:
    if p.suffix == ".pdf":
        return extract_pdf_text(p, max_pages=40)
    t = p.read_text(encoding="utf-8", errors="replace")
    return clean(re.sub(r"<!--.*?-->", "", t, flags=re.S))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--chroma-path", default=DEFAULT_CHROMA_PATH)
    ap.add_argument("--collection", default=COLLECTION)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--batch-size", type=int, default=4)
    ap.add_argument("--timeout", type=float, default=900)
    a = ap.parse_args()

    docs = collect()
    records = []
    for repo, p, kind, tier in docs:
        body = text_of(p)
        if not body:
            continue
        repo_name = repo.name if repo != HOME else "home"
        rel = str(p.relative_to(repo))
        digest = hashlib.sha256(p.read_bytes()).hexdigest()
        commit = git_commit(repo)
        for n, piece in enumerate(chunk(body)):
            records.append((
                f"stream::{repo_name}::{rel}::{n}",
                f"[SocrateAI stream | {kind} | {repo_name}/{rel}]\n\n{piece}",
                {"corpus": "qc_streams", "source_kind": kind, "repo": repo_name, "path": rel,
                 "chunk": n, "git_commit": commit, "sha256": digest, "tier_note": tier,
                 "provenance": "SocrateAI stream writing; AI-assisted; NOT peer-reviewed literature"}))
    print(f"{len(docs)} documents -> {len(records)} chunks")
    if a.dry_run:
        for repo, p, kind, _ in docs:
            print(f"  {kind:20} {p}")
        return 0

    embedder = load_anse_embedding_function()(timeout_s=a.timeout, max_retries=2)
    probe = embedder.probe()
    print(f"embeddings: {probe['model']} -> {probe['dimension']}-d", flush=True)
    import chromadb
    col = chromadb.PersistentClient(path=a.chroma_path).get_or_create_collection(
        name=a.collection, embedding_function=embedder, metadata={"hnsw:space": "cosine"})

    digests = {r[0]: r[2]["sha256"] for r in records}
    existing = col.get(include=["metadatas"])
    stale = [i for i, m in zip(existing["ids"], existing["metadatas"])
             if digests.get(i) != m.get("sha256")]
    if stale:
        col.delete(ids=stale)
        print(f"removed {len(stale)} stale chunks")
    fresh = set(existing["ids"]) - set(stale)
    todo = [r for r in records if r[0] not in fresh]
    for s in range(0, len(todo), a.batch_size):
        b = todo[s:s + a.batch_size]
        col.upsert(ids=[r[0] for r in b], documents=[r[1] for r in b], metadatas=[r[2] for r in b])
        print(f"  upserted {min(s + a.batch_size, len(todo))}/{len(todo)}", flush=True)
    print(f"collection '{a.collection}' holds {col.count()} chunks; store {a.chroma_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
