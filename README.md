# SocrateAI-Scientific-QuantumComputing

**QC Stream 1: planar universal optimality → quantum hardware.**
Status (2026-10-11): **prepared, not implemented.** Not peer reviewed.

This stream turns earlier SocrateAI results into verification tools for quantum hardware and software. The source
results are:
- Lean corollaries of an AI-generated planar universal-optimality theorem;
- a Lean proof that gated image-charge kernels are completely monotone;
- Rust N-body solvers with a one-sided energy floor check.

The target applications are:
- a Riesz-6 (Rydberg C₆/r⁶) verification benchmark on analog neutral-atom hardware;
- a gate-safe operating envelope for gated Wigner and exciton crystals;
- an energy-floor check for VQE and error-mitigated estimates.

Every Lean-derived claim here is **conditional** on the unreviewed upstream theorem
`OAI.AtomicTriangular.universal_energy_minimum` (github.com/openai/math). The 2D Cohn–Kumar conjecture is still open
in the peer literature.

## Documents

| File | Content |
|---|---|
| [docs/QC_STREAM1_BRAINSTORM.md](docs/QC_STREAM1_BRAINSTORM.md) | original brainstorm (verbatim), review questions, dated update |
| [docs/QC_STREAM1_WORKFLOW.md](docs/QC_STREAM1_WORKFLOW.md) | phases P0–P5, preregistration stubs, owed items |
| [docs/LITERATURE_REVIEW.md](docs/LITERATURE_REVIEW.md) | 73-paper first pass, findings F1–F12, revised verdict per idea |
| [docs/DEPENDENCIES.md](docs/DEPENDENCIES.md) | local artifacts, Zenodo records, third-party software, hardware facts |

## Layout

```
corpus/      literature + sibling-stream ingestion into the ANSE Chroma store (qc_literature, qc_streams)
papers/      index.json + meta/ (PDFs are fetched locally, git-ignored)
docs/        planning documents
lean/        (P1, not started)  Lean lemmas: gate-kernel admissibility, finite-N floor
solvers/     (P2–P4, not started) classical baselines; bindings to rusty-SUNDIALS qf-yukawa-crystal
hardware/    (P2, not started) Braket AHS / bloqade-analog encodings, emulator first
prereg/      (per phase) preregistrations, hypothesis + kill criterion, written before code
```

## Rebuilding the literature index

```bash
PY=~/AutoevolveAI/.venv/bin/python             # has chromadb; needs Ollama with qwen3-embedding:0.6b
$PY corpus/fetch_papers.py                     # arXiv metadata + PDFs, fails closed on title mismatch
$PY corpus/ingest_chroma.py --resume           # -> collection qc_literature
$PY corpus/ingest_streams.py                   # -> collection qc_streams (SocrateAI writing, not peer reviewed)
$PY corpus/query_chroma.py --verify            # acceptance probes
```
