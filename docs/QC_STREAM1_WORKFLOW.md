# QC Stream 1 — Workflow: planar universal optimality → quantum hardware

**Status (2026-10-11):** project **prepared, not implemented**.
- Phases P0 (preparation) is ✅; P1–P5 are ⛔ not started.
- No Lean, Rust or quantum-SDK code exists in this repository yet.

Inputs to this plan:
- [QC_STREAM1_BRAINSTORM.md](QC_STREAM1_BRAINSTORM.md): ideas, recorded verbatim;
- [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md): findings F1–F12;
- [DEPENDENCIES.md](DEPENDENCIES.md): materials and versions.

Conventions, taken from LeanMaster:
- Tiers: **A** kernel-checked, **L** literature, **N** numerical, **C** conjecture.
- **Every Tier A claim in this stream is conditional** on the unreviewed upstream theorem `OAI.AtomicTriangular.universal_energy_minimum`. Statement fidelity (red-team target T1) is still open.
- Never write "zero axioms" or "fully verified". The correct wording is "depends only on `propext`, `Classical.choice`, `Quot.sound`".
- No Lean result is claimed until `lean-proof-gate` passes. Corrections go next to the original; nothing published is rewritten.
- Numbering: "QC Stream 1" is independent of LeanMaster's Stream 1–5 and of the K3 programme's streams.

---

## 1. Why this stream exists

Earlier SocrateAI streams produced four things this stream can use:
- kernel-checked corollaries of a planar universal-optimality theorem: Riesz s > 0, any density, a vacancy non-uniqueness result;
- a Lean proof that gated image-charge kernels stay completely monotone;
- a Rust N-body solver with a one-sided `floor_check`;
- preregistered evidence that annealing gets trapped for soft Yukawa interactions.

Quantum hardware has two features this work speaks to. Rydberg atoms interact via C₆/r⁶ (Riesz s = 6), and electrons, ions and excitons sit near metal gates. This stream turns those results into **verification tools** for quantum hardware and software. It does not claim quantum advantage (F4).

## 2. Motivation (Tier C — recorded, not asserted)

See the brainstorm §2.1. The literature review (§2 there) re-scores the five ideas:
- 1 → reframe as a verification benchmark;
- 2 → narrow;
- 3 → rewrite or drop;
- 4 → strongest;
- 5 → narrow tool.

The phases below follow that ranking.

## 3. Phases

Each phase starts with a preregistration (`prereg/QC1-Pn.json`, same format as `triangular-universal-optimality-lean/prereg/`), written **before** any code. The stubs below fix the hypothesis and the kill criterion now.

### P0 — Preparation ✅ (this commit)
- Repository skeleton, brainstorm, literature review, dependency map.
- Chroma collections `qc_literature` and `qc_streams`.

### P1 — Statement audit and potential coverage (Lean; first, because everything depends on it)
- **P1.1** Re-run `lean-proof-gate` on `triangular-universal-optimality-lean` (v0.3.0) against openai/math `fd4aeeb2` and record the result here. Read RED_TEAM T1 status.
- **P1.2** New lemma, Tier C → A target: the single-plane image potential f(t) = t^(−1/2) − (t+4d²)^(−1/2) satisfies upstream `AdmissiblePotential`, because (−1)ᵏf⁽ᵏ⁾ ∝ t^(−1/2−k) − (t+4d²)^(−1/2−k) ≥ 0.
- **P1.3** Locate and pin the 52-theorem dual-gate kernel module from SocrateAI-Scientific-QuantumFluids (Zenodo 23297479). Check whether its CM notion matches upstream `AdmissiblePotential` (a function of r², smooth on (0,∞)), and whether a bridge lemma gives the gated **exciton** kernel as a corollary of D1/D2.
- **P1.4** Check that Riesz s = 6 with a hard-core cut-off (blockade) is **not** admissible. A plateau potential breaks complete monotonicity (F3). Record exactly what the D1 claim covers on hardware.
- *Prereg stub.* H: the P1.2 kernel is admissible, and D1 covers bare C₆/r⁶. Kill: any `AdmissiblePotential` clause fails for the gate kernel at some d > 0, or statement fidelity T1 is refuted.

### P2 — Verification benchmark on a Riesz-6 lattice gas (idea 1, reframed)
- **P2.1 Encoding.**
  - Candidate sites form a fine grid, triangular or square, with spacing ≥ 4 µm (Aquila).
  - Variables are Rydberg occupations.
  - Energy is −Δ·N_R plus Σ C₆/r⁶ over pairs of Rydberg atoms. Choose Δ to fix the density.
  - Target: the triangular sub-lattice arrangement.
  - Caveat: the theorem is a continuum, infinite-volume statement (F1, F5). The ground state of the **discrete, finite** problem must be fixed independently, by exact enumeration or ILP for small N.
- **P2.2 Classical baselines**, in `qf-yukawa-crystal`, adapted to s = 6 on sites:
  - simulated annealing;
  - parallel tempering;
  - basin hopping;
  - exact ILP/branch-and-bound;
  - the UDG-MIS solvers of 2307.09442.

  Rønnow-style time-to-target metrics (1401.2910). Finish the owed full-budget κ=1 runs first, and publish the r_c erratum for Zenodo 23293429.
- **P2.3 Emulation:** Braket local `braket_ahs` and bloqade-analog, N ≤ 12–16. Only then use Aquila (256 sites, $0.30/task + $0.01/shot). D-Wave via Leap and Pasqal via its own cloud are optional, because neither is on Braket.
- **P2.4 Analysis:** compare the probability of the target configuration against classical time-to-target, and run `ubound.py` on measured snapshots.
- *Prereg stub.* H: on hard instances where SA fails, defined by the P2.2 suite, the analog run reaches the target with probability above the classical success rate at matched wall-clock. Kill: tempering or ILP solves every instance up to device size (no hard instances, as in F4), **or** the emulator ground state differs from the triangular target.

### P3 — Gate-safe operating envelope (idea 4)
- **P3.1** State the envelope precisely. With P1.2 and P1.3 done, the classical bulk ground state of the gated crystal is triangular, conditional on upstream, for every gate distance. This covers the many-electron and exciton **crystal** phases, not single-electron trap qubits (F11).
- **P3.2** Numerical cross-check: gated Coulomb crystal energies against the Lean floor, using `floor_check` with the exact image sum (not shifted-force).
- **P3.3** Join the gated-exciton Lindemann result (d/a_M ≳ 49) to literature melting criteria (F10). The aim is a statement about which failures the envelope excludes, not a claim that melting is "exonerated".
- *Prereg stub.* H: no gated configuration in the test family is reported below the Lean floor once truncation tails are bounded. Kill: a floor violation that survives the `tail_bound` correction.

### P4 — Energy-floor check for VQE and error mitigation (idea 5, narrowed)
- **P4.1** Finite-N lower bound for a CM pair potential in a box or trap, with boundary terms. This is a new theorem target; without it, idea 5 is not usable on hardware-size problems.
- **P4.2** Python/Rust binding of `check_reported_energy`, designed as a callback for qiskit-algorithms VQE and for mitigated (ZNE/PEC) estimates.
- **P4.3** Compare against SDP/RDM lower bounds (F12) on the same small instances, to measure what the geometric floor adds.
- *Prereg stub.* H: for first-quantised position Hamiltonians H = T + V with V completely monotone, mitigated estimates falling below the floor are detected at a rate matching the injected noise. Kill: the floor is looser than the SDP bound on every test instance, which would make it redundant.

### P5 — Defects and layouts (ideas 2 and 3, narrowed; lowest priority)
- **P5.1** Layout note: color-code-compatible triangular/hexagonal arrays and 2D ion crystals. Lattice geometry versus Coulomb (not covered) is stated explicitly.
- **P5.2** Defect note: what D3 states (liminf energy density) versus formation energy and mobility (F8, F9). No qubit or braiding claim unless a twist-defect construction (1004.1838) is involved.
- *Prereg stub.* None until P1–P4 report.

## 4. Out of scope for P0 (deliberately not done)

Lean files, a lakefile, Rust crates, Braket/Bloqade/Pulser programs, QPU submissions, any new Zenodo deposit, and any outreach.

## 5. Owed items inherited from sibling streams

- Full-budget κ=1 basin-hopping and tempering runs (rusty-SUNDIALS `qf-yukawa-crystal`).
- r_c = 8 truncation erratum for Zenodo 23293429.
- Merge of `physics/ubound.py` (triangular-UO branch `docs/physicist-guide`).
- Jellium main-run output (J1).
- LeanMaster `declarations.db` re-index, so that the D1–D3 corollaries become searchable there.
