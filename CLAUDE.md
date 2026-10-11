# CLAUDE.md — SocrateAI-Scientific-QuantumComputing

- Read `docs/QC_STREAM1_WORKFLOW.md` first. It holds the phases, the status and the owed items.
- Epistemic tiers: A (kernel-checked, name the declaration), L (literature, give the arXiv id or DOI), N (numerical), C (conjecture).
- **Every Tier A claim is conditional** on the unreviewed upstream `OAI.AtomicTriangular.universal_energy_minimum` (openai/math `fd4aeeb2`).
  Never present 2D Cohn–Kumar as proved.
- Never write "zero axioms", "fully verified" or "guarantees". Say "depends only on `propext`, `Classical.choice`, `Quot.sound`".
  Load the `lean-proof-gate` skill before claiming any Lean result.
- Covered potentials: Gaussian and Riesz s > 2 (incl. Rydberg s = 6, dipolar s = 3) are Tier A (conditional). Yukawa is Tier C.
  Coulomb (s = 1) and Lennard-Jones are not covered.
- Preregister each phase (`prereg/`) before writing code. Never rewrite a published artifact; add corrections beside it.
- Vector DB: ANSE Chroma at `~/AutoevolveAI/data/chroma`, collections `qc_literature` (peer literature) and `qc_streams`
  (SocrateAI writing). Do not mix the two, and do not write to other collections.
- The Python with chromadb is `~/AutoevolveAI/.venv/bin/python`. Embeddings come from Ollama `qwen3-embedding:0.6b` (1024-d).
- `rm -rf` is denied for this user; move things aside instead.
