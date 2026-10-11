# QC Stream 1 — Dependencies and materials

**Status (2026-10-11):** inventory only. Nothing here is vendored, built or installed yet.
`~` = `/home/callensxavier_gmail_com`; `AE` = `~/AutoevolveAI/.claude/worktrees/openai-math-discovery`;
`DISK` = `/mnt/disks/disk-socrateai-local-1`.

Tiers: **A** kernel-checked (conditional where noted) · **L** literature · **N** numerical · **C** conjecture / written argument.

---

## 1. Mathematical base (everything below is conditional on this)

| Item | Where | Status |
|---|---|---|
| Upstream theorem `OAI.AtomicTriangular.universal_energy_minimum` (module `OAI.Analysis.Triangular.Energy.Universal`) | github.com/openai/math (Apache-2.0), commits `adc7f1241b42e322a6451854ab7e4b4c146bf78a` (initial, 2026-10-06) and `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` (HEAD, 2026-10-08); the key files have the same blob at both. Local vendored copy: `~/SocrateAI-Scientific-Agora-LeanMaster/lean4basesource/openai-math/lean/OAI/Analysis/Triangular/` | Kernel-accepted, **AI-generated, not peer reviewed**. The 2D Cohn–Kumar conjecture is still open in the peer literature (arXiv:2511.03353, 2025). |
| `AdmissiblePotential g` := smooth on (0,∞), g ≥ 0, (−1)ʳ g⁽ʳ⁾ ≥ 0, a function of the **squared** distance; `energy` = liminf of disk energies | `.../OAI/Analysis/Triangular/Energy/Basic.lean:26` | definition; statement fidelity is target T1 of the red-team review (no human check yet) |
| Toolchain | `leanprover/lean4:v4.34.1`, mathlib `v4.34.1` (2026-09-24) | — |
| Upstream manuscripts (family 090: universal optimality, atomic certificate, Coulomb-renormalized, sharp-Fourier) | `.../openai-math/preprints/` | Tier L (unrefereed). Coulomb/jellium appears only in the manuscript (§8), not in Lean. |

## 2. SocrateAI Lean corollaries — `~/triangular-universal-optimality-lean` (MIT, tag v0.3.0)

All of these are kernel-checked with axioms {`propext`, `Classical.choice`, `Quot.sound`}, are **conditional on §1**, and were rebuilt on 2026-10-11 (`verification/rebuild_2026-10-11/SUMMARY.md`). They were checked by an independent AI verifier, not by a human.

| ID | Declaration (file under `lean/Triangular/`) | Use in QC Stream 1 |
|---|---|---|
| D1 | `TriangularRiesz.riesz_admissible`, `triangular_riesz_optimal` (`Riesz.lean`), any `s > 0` | **Riesz s = 6 = Rydberg C₆/r⁶ van der Waals**: idea 1 target potential |
| D1b | `latticeEnergy_riesz_lt_top` (`RieszFinite.lean`), `s > 2` | makes D1 non-vacuous for s = 6 and the dipolar case s = 3 |
| D2 | `triangular_optimal_any_density`, `unscaled_false` (`AnyDensity.lean`) | the floor at a physical density ρ |
| D3 | `triangular_universally_optimal`, `vacancy_energy`, `vacancy_universally_optimal`, `vacancy_not_isometric_image`, `universal_optimum_not_unique` (`UniversalOptimality.lean`) | idea 3; **liminf (lower-energy) sense only**; non-uniqueness means "known ground state" is not unique |
| D4 | `universal_energy_minimum_open` (`OpenDisk.lean`, `OpenDiskAny.lean`) | robustness of the formal statement only |

Mirrors: `AE/formal_cert/Triangular/`; `DISK/leanmaster/contrib-openai-math-2026-10-10/contrib/openai_math_corollaries/` (no D4). LeanMaster releases v3.47.0–v3.48.1 ship D1–D3. LeanMaster's own theorem index (`.leancache/declarations.db`, 900 declarations, built 2026-09-17) predates these and does not list them.

Potentials **not** covered by Lean: Yukawa (Tier C: `ex:ch4-yukawa` in the textbook and the YUK-TRI-1 prereg), **Coulomb s = 1** (outside D1's finite range; renormalized version only in the upstream manuscript), Lennard-Jones (not completely monotone).

## 3. Gated-kernel results (idea 4) — `SocrateAI-Scientific-QuantumFluids`

| Item | Where | Status |
|---|---|---|
| Image-charge series from grounded gates keeps the **dipolar exciton** kernel completely monotone in r² (Poisson summation) | Zenodo 10.5281/zenodo.23294615 (*Gated exciton fluids I*) | paper proof (Tier C/L) |
| Dual-gated bilayer image kernel = Laplace transform of a non-negative density, hence CM; 52 theorems | Zenodo 10.5281/zenodo.23297479 (*Gated exciton fluids II*); GitHub `xaviercallens/SocrateAI-Scientific-QuantumFluids` | Lean, verified by an independent AI verifier. **Not present in the local disk copy** `DISK/leanmaster/SocrateAI-Scientific-QuantumFluids` (only `GPGalerkin`, `QuantumFluidsShell`); module name to pin from GitHub |
| Harmonic Lindemann estimate: a rigid exciton crystal needs d/a_M ≳ 49; gates only raise it | same record, WP2 | negative numerical result (N) |
| Single grounded plane for a **bare charge**: f(t) = t^(−1/2) − (t+4d²)^(−1/2) | textbook `AE/papers/textbook_universal_optimality/ch4_physics.tex` ≈ l.462–470, `ex:ch4-image` (Tier C, no CM claim) | (−1)ᵏf⁽ᵏ⁾ ∝ t^(−1/2−k) − (t+4d²)^(−1/2−k) ≥ 0, so it is CM: a **two-line Tier C argument**, candidate lemma for this stream |
| QuantumFluids library v1.21.0 (235 theorems) | Zenodo 10.5281/zenodo.23292863 (MIT) | supporting |

## 4. Numerical artifacts (Rust, rusty-SUNDIALS, BSD-3-Clause)

Crate `qf-yukawa-crystal`, in `~/rusty-SUNDIALS-wt-yukawa-global/crates/qf-yukawa-crystal/` (rusty-SUNDIALS v11.7.0, commit 47ef504). It is **not** on the `~/rusty-SUNDIALS` main checkout, which is on branch `merge-mcp-temp`.

| Function / file | Idea | Status / caveat |
|---|---|---|
| `src/lib.rs`: `relax` (CVODE BDF), `anneal`, `hessian`, `order` | 1, 2 | N |
| `src/global_opt.rs`: `basin_hopping`, `parallel_tempering` | 1 | N. A short κ=1 run did not beat the quench; **full-budget runs are still owed** |
| YUK-TRI-1 prereg `results/preregistration.json`; `results/summary_stdout.txt` | 1 | At κ=1, annealing reached the lattice in **0/10** OC20 starts (prediction FAILED); it passes at κ=2. Hard starts: uniform_03/08/09, oc20_02/04/05/08/09. Do **not** claim the runs prove ODE solvers insufficient |
| `results/controls.jsonl` `ctl_neg_square_saddle` | 2 | square lattice: 72 negative Hessian modes at κ=2, 64 at κ=1 (min −0.53) |
| `~/rusty-SUNDIALS-wt-jellium/.../results/jellium/controls.jsonl` | 2 | jellium square saddle, 64 negative modes; Madelung energy matches Bonsall–Maradudin to ~1e-10; main J1 run output not found |
| `floor_check(sys, x, r_exact)`, `check_reported_energy(kappa, rho, e_reported, r_exact)`, `tail_bound`, `triangular_energy_exact`, `periodic_energy_exact` | 5 | unit-tested. **One-sided**: a violation shows a bug, a pass proves nothing. Periodic geometry only; must use the exact (not shifted-force) potential. CLI `yukawa_crystal floor <crate_dir> [kappa] [csv...]` |
| **Erratum owed** to Zenodo 23293429 | 1 | r_c = 8 truncation shifts energies by 1.8e-2 at κ=1, more than the triangle–square gap |

## 5. Python tools worth reusing

- `~/triangular-universal-optimality-lean/.claude/worktrees/physics-skyrmion/physics/ubound.py`: tests any 2D point file against the floor, using a Voronoi density estimator and matched controls; has `--self-test`. It lives on unmerged branch `docs/physicist-guide`. A natural post-processor for QPU or annealer snapshots.
- `AE/papers/textbook_universal_optimality/code/quantum_melting.py` (zero-point motion, Lindemann), `ch3_yukawa_small.py`, `fss_disk.py`.
- `AE/papers/universal_optimality_tiered/lab/lab_analysis.py`: lab protocols L1–L4 (L4 = electrons on helium).
- LeanMaster gate tools `~/SocrateAI-Scientific-Agora-LeanMaster/tools/{axiom_audit,statement_lock,sorry_grep,phrasing_lint}.py`, and the skills `lean-proof-gate` and `lean-tiered-proving`.
- `~/triangular-universal-optimality-lean/tools/lean_pinned.py`; `~/verify_triangular_uo.sh`.
- Corpus pipeline (this repo, `corpus/`): adapted from CondensedMatterTheory `adscmt-litreview`.

## 6. Zenodo records

**Own (creator Callens, Xavier; CC-BY-4.0 unless noted):**

| DOI | Title (short) | Role here |
|---|---|---|
| 10.5281/zenodo.23285631 | Riesz-energy, finiteness and every-density corollaries (D1/D1b/D2) | base corollaries |
| 10.5281/zenodo.23293429 (v2; v1 23293112; concept 23293111) | Planar universal optimality, tiered (D3, CVODE N-body Yukawa check, lab protocols) | idea 1 evidence; erratum owed |
| 10.5281/zenodo.23295142 | *The Triangular Lattice and Universal Optimality* (textbook, 105 pp) | pedagogy; Tier C image-charge exercise |
| 10.5281/zenodo.23289027 | Testing a planar lattice-optimality theorem against an exciton-fluid interaction | idea 4 background |
| 10.5281/zenodo.23294615 | Gated exciton fluids I (image charges preserve CM) | idea 4 |
| 10.5281/zenodo.23297479 | Gated exciton fluids II (Lean kernel theorem, Lindemann) | idea 4 |
| 10.5281/zenodo.23298292 | Gated exciton fluids III (Newton–Krylov, Fenris-CMRR) | idea 4 |
| 10.5281/zenodo.23292863 | QuantumFluids Lean library v1.21.0 (MIT) | library |

**Third-party:**

| DOI | Content | License | Use |
|---|---|---|---|
| 10.5281/zenodo.6462687 | Ebadi et al. Rydberg-MIS data and code | CC-BY-4.0 | idea 1 baseline / encoding reference |
| 10.5281/zenodo.16107683 | Penning-trap planar ion crystal code and data (PRA 2025) | MIT | idea 2, real triangular Coulomb crystals |
| 10.5281/zenodo.4450305 | Skyrmion lattice positions (Zázvorka/Dittrich) | CC-BY-4.0 | `ubound.py` case study |
| 10.5281/zenodo.17063771, 18111798 | Skyrmion orientation; FeGe disclinations | CC-BY-4.0 | defect data (idea 3) |
| 10.5281/zenodo.20273182 | Wigner-crystal polarons in a TMD monolayer (2026) | CC-BY-4.0 | idea 4 |
| 10.5281/zenodo.20423683 | Campaioli, validation and calibration of quantum hardware (2026) | CC-BY-4.0 | idea 1/5 methodology |
| 10.5281/zenodo.22661068, 22690145 | Pulser v1.9.1; Pasqal emulators v2.10.0rc1 | Apache-2.0 / CC-BY-4.0 | emulation |

## 7. Third-party software to depend on (versions as of 2026-10-11)

| Package | Version | License | Role |
|---|---|---|---|
| amazon-braket-sdk-python | 1.127.3.post0 | Apache-2.0 | AHS programs for QuEra Aquila |
| amazon-braket-default-simulator-python | 1.40.2 (local `braket_ahs`) | Apache-2.0 | free local emulation, run before any QPU |
| amazon-braket-examples (`examples/analog_hamiltonian_simulation/` 01, 02, 03, 05, 09) | no tags | Apache-2.0 | templates |
| QuEraComputing/bloqade-analog | 0.16.9 | Apache-2.0 | alternative AHS front end and emulator |
| pasqal-io/Pulser; pasqal-cloud | 1.9.1; 0.24.0 | Apache-2.0 | Pasqal (**not on Braket**; via its own cloud, Azure, OVHcloud, Scaleway, GCP) |
| dwave-ocean-sdk; dwave-samplers; dwave-system | 9.5.0; 1.8.0; 1.36.0 | Apache-2.0 | D-Wave via Leap (**not on Braket**); use `dwave-samplers`, not frozen `dwave-neal` |
| qiskit; qiskit-algorithms; qiskit-nature | 2.5.2; 0.4.0; 0.8 | Apache-2.0 | VQE side of idea 5 |
| Cirq; OpenFermion | 1.7.0; 1.8.1 | Apache-2.0 | alternative VQE stack |
| thefundamentaltheor3m/Sphere-Packing-Lean | HEAD 2026-10-08 | Apache-2.0 | reference formalisation (Viazovska dim 8) |
| lammps (yukawa pair style) / hoomd-blue 7.2.0 / sarkas 1.0.0 | — | GPL-2.0 / BSD-3 / MIT | independent classical baselines |
| WesLeeJohnson/mode_analysis; kmoskovtsev/Electrons-on-Helium-Scripts | — | GPL-3.0 / **no license** | Penning modes; e⁻-on-He scripts (study only) |

## 8. Hardware facts (idea 1)

From the amazon-braket-examples notebook `01_Introduction_to_Aquila` output. These are **not** live `GetDevice` data; re-query before any submission.

- Device ARN: `arn:aws:braket:us-east-1::device/qpu/quera/Aquila`.
- Geometry:
  - up to 256 sites in a 75 × 76 µm field of view;
  - minimum spacing 4 µm, position resolution 0.01 µm;
  - position error about 0.2 µm; filling error about 0.8% (worst case 5%).
- Rabi frequency 0–15.8 Mrad/s; global detuning ±125 Mrad/s; drive duration up to 4 µs; time step 50 ns.
- Local detuning is experimental and needs Braket Direct.
- Price: $0.30 per task plus $0.01 per shot (pricing page, 2026-10-11); 1–1000 shots per task.

**Encoding consequence.** Atom positions are classical parameters fixed before the run, and the interaction exists only between atoms in the Rydberg state. The QPU therefore cannot relax continuous positions. Idea 1 has to be posed as Rydberg occupation (a lattice gas / MIS problem) on a fine grid of candidate sites, with C₆/r⁶ = Riesz s = 6 as the native potential. See `QC_STREAM1_WORKFLOW.md` P1.2.
