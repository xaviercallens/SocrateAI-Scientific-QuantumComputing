# QC Stream 1 — From Planar Universal Optimality to Quantum Hardware (Brainstorm)

**Status (2026-10-11):** brainstorm recorded, **unreviewed**. No phases opened yet. Nothing in this
document is kernel-checked inside this repository.

> Naming: "QC Stream 1" is this repository's own numbering. It is independent of LeanMaster's
> Stream 1–5 numbering and of any other SocrateAI programme's streams.

Epistemic tiers used below (same convention as LeanMaster):
**A** = kernel-checked Lean 4 result (passes `lean-proof-gate`), **L** = published literature,
**N** = numerical evidence (solver output, not a proof), **C** = conjecture / motivation, recorded not asserted.

---

## 1. Why this stream exists

Leading quantum hardware platforms all involve 2D or quasi-2D systems of mutually repelling
particles. Examples are trapped ions (2D Penning-trap crystals), electrons floating on liquid helium,
and Rydberg-interacting neutral atoms. Earlier SocrateAI streams studied the classical energy
landscape of exactly these systems:
- discrete geometry: Cohn–Kumar universal optimality in the plane, formalized in Lean 4;
- mean-field and fluid dynamics, with Rust solvers (rusty-SUNDIALS).

This stream asks whether those results can be turned into **tools for quantum hardware and quantum
software**:
- benchmarks with a known ground state;
- layout guidance;
- error-detection floors for noisy energy estimates.

## 2. Motivation (Tier C — recorded, not asserted)

### 2.1 Original brainstorm (verbatim, as submitted)

Moving from classical discrete geometry and mean-field fluid dynamics into Quantum Computing (QC) might seem like a leap at first. However, the physical hardware of quantum computers—whether trapped ions, electrons floating on liquid helium, or neutral Rydberg atoms—relies fundamentally on the 2D interaction of mutually repelling particles.

By applying the rigorous bounds of the Cohn-Kumar planar universal optimality theorem and our epistemic pipeline (Lean 4 + Rust solvers), we can stop guessing how these physical substrates want to behave classically, and instead use that mathematical certainty to engineer more stable quantum hardware.

Here is a deep-thinking brainstorming session outlining 5 ways the findings from these papers could directly advance Quantum Computing.

#### 1. A Mathematically Certified Benchmark for Quantum Advantage

**The Insight:** In our numerical experiments (rusty-SUNDIALS), classical ODE solvers and simulated annealing failed catastrophically to find the triangular ground state for "soft" interactions (like the κ=1 Yukawa potential). They got trapped in glassy, defected local minima because the mathematical energy landscape is incredibly flat and vast.

**The QC Application:** Analog quantum simulators (like Pasqal's or QuEra's neutral atoms) and Quantum Annealers (like D-Wave) are designed to use quantum tunneling to bypass these exact types of glassy, classical local-minima traps. But proving they actually do this better than classical computers is notoriously difficult because we rarely know the true ground state of an N-body system.

**The Innovation:** The AI-generated, Lean-verified Cohn-Kumar theorem gives us the ultimate "cheat code." Because we know the exact absolute ground state is the perfect triangular lattice, we can program a quantum simulator with a completely monotone soft potential. If the quantum hardware can reliably tunnel into the perfect triangular lattice while classical supercomputers remain trapped, we have an undeniable, mathematically certified demonstration of Quantum Advantage for continuous geometric optimization.

#### 2. Passive Self-Assembly for Qubit Scaling (Fighting the Square Grid)

**The Insight:** The theorem guarantees that any planar system of particles interacting via a completely monotone potential (like Coulomb or van der Waals) will unconditionally seek a triangular lattice. The numerical controls also proved the square lattice is a highly unstable saddle point with dozens of negative Hessian eigenvalues.

**The QC Application:** Companies building neutral atom or trapped ion arrays use incredibly complex active laser systems (optical tweezers) to force qubits into 2D arrays—often attempting to build square grids to match standard quantum circuits. Fighting thermodynamics to hold repelling qubits in a square grid introduces immense physical stress, requiring higher laser power and leading to phononic noise (vibrational decoherence).

**The Innovation:** If QC hardware transitions natively to triangular/hexagonal optical tweezer arrays, the physical layout aligns exactly with the universal thermodynamic minimum. Hardware designers could leverage passive self-assembly: by applying a simple global confining trap and letting the atoms cool, the mathematics guarantees they will auto-assemble into a flawless triangular lattice. (Conveniently, Topological Color Codes for error correction map perfectly onto hexagonal/triangular lattices).

#### 3. "Zero-Cost" Defect Qubits for Topological Braiding

**The Insight:** Chapter 2 formalized the "Vacancy Theorem" (D3) in Lean 4, proving a highly counter-intuitive fact: a triangular lattice with exactly one missing particle (a vacancy) possesses the exact same macroscopic minimum lower-energy density as a flawless lattice.

**The QC Application:** Topological quantum computing relies on moving "holes" or quasiparticles around each other (braiding) to execute quantum gates that are immune to local noise.

**The Innovation:** If we use a 2D Wigner crystal (like a gated TMD exciton fluid or electrons on liquid helium) as a qubit substrate, the Lean 4 proof guarantees that introducing vacancies does not pump macroscopic thermodynamic energy into the lattice. These highly stable vacancy defects can act as robust, isolated qubits. Because they cost "zero" bulk energy, quantum engineers could theoretically program dynamic routing paths to gently push these vacancies through the rigid crystal to execute topological braiding, without the risk of melting the surrounding bulk crystal.

#### 4. De-Risking Metal Gate Architectures (Electrons on Helium)

**The Insight:** In our fourth preprint, we used Poisson summation to prove that adding an infinite series of alternating image charges from grounded metallic plates does not break the "completely monotone" requirement of the potential.

**The QC Application:** "Electrons on liquid helium" and solid-state spin qubits are highly promising QC architectures. To control these qubits and execute gates, engineers must pack dense grids of metallic electrodes nanometers away from the quantum fluid. A major fear has been that complex metallic screening will create attractive interference, destroying the stability of the underlying electron crystal.

**The Innovation:** This proof provides a mathematically protected operating envelope for quantum chip architects. It mathematically guarantees that no matter how close or complex the grounded metallic gates are, they cannot classically destroy the fundamental optimality of the 2D fluid. If an experimentalist observes the lattice melting in the lab, they instantly know the cause is quantum zero-point fluctuations (the Lindemann melting criterion) or thermal noise, because the classical bulk electrostatics have been exonerated.

#### 5. Verified "Floor Checks" for Quantum Compilers (VQE Mitigation)

**The Insight:** In the Rust numerical solver, a strict `floor_check` was implemented. If the solver calculated an energy lower than the Lean-verified lattice energy, the code instantly knew it had suffered an algorithmic truncation error, not a physics breakthrough.

**The QC Application:** In the NISQ (Noisy Intermediate-Scale Quantum) era, algorithms like the Variational Quantum Eigensolver (VQE) are used to find the ground-state energy of interacting particle systems. Because of hardware noise, QPUs often hallucinate and output unphysical, mathematically impossible energies.

**The Innovation:** We can port our Lean 4 epistemic pipeline into Quantum Compilers (like Qiskit or Cirq). If a quantum programmer asks the QPU to simulate a 2D interacting system governed by a completely monotone potential, the compiler uses the Cohn-Kumar limit as a hard baseline unit test. If the quantum hardware outputs an energy lower than the Lean 4-verified triangular lattice floor, the compiler instantly flags a quantum hardware hallucination or decoherence event. This serves as a mathematically absolute penalty for quantum machine learning loss functions, strictly bounding quantum noise.

#### An Open Call for Collaboration

By linking formal discrete geometry to quantum hardware, we aren't just doing abstract math—we are describing the physical "canvas" upon which future qubits will be painted.

To the quantum information theorists, neutral-atom experimentalists, and quantum compiler engineers in the community: Does this framework map onto your current bottlenecks?

The most immediate, executable project here is #1 (Benchmarking Quantum Simulators). Could we translate our soft Yukawa Hamiltonian into a concrete pulse sequence that can be run on an open-access neutral atom quantum computer (like Pasqal or QuEra via AWS Braket) to test if the QPU avoids the glassy traps our classical Rust solver fell into?

---

## 3. Reuse map — what each idea borrows from other streams

Artifact locations below were checked on 2026-10-11 under restricted tooling, without directory
search. "Not located" means **not yet found**, not "does not exist". Fill these in during review.

| # | Idea | Reuses (claimed source) | Artifact location | Tier today |
|---|------|-------------------------|-------------------|------------|
| 1 | Certified benchmark for quantum advantage | rusty-SUNDIALS κ=1 Yukawa runs (SA / ODE trapped in glassy minima); Cohn–Kumar planar optimality | `~/rusty-SUNDIALS/` exists (Rust CVODE port, Lean specs in `proofs/lean4/`); Yukawa/annealing runs **not located** | N (runs) · see §4 for the theorem |
| 2 | Triangular layouts / self-assembly | Cohn–Kumar planar optimality; square-lattice Hessian saddle (negative eigenvalues) | Hessian control run **not located** | N (Hessian) · C (hardware claim) |
| 3 | Vacancy defect qubits | "Vacancy Theorem" D3 (Lean 4, Chapter 2) | **not located** | claimed A, unverified here |
| 4 | Metal-gate envelope (e⁻ on He) | Preprint #4: image-charge series via Poisson summation stays completely monotone | preprint **not located** | claimed A/L, unverified here |
| 5 | Floor checks for VQE / compilers | Rust `floor_check` + Lean-verified lattice energy | `floor_check` **not located** | N (implementation) · C (compiler port) |
| — | Proof-gate tooling | LeanMaster `tools/axiom_audit.py`, `statement_lock.py`, `sorry_grep.py`, `phrasing_lint.py`; skills `lean-proof-gate`, `lean-tiered-proving` | `~/SocrateAI-Scientific-Agora-LeanMaster/tools/` | reusable as-is |

**Action for review:** replace every "not located" with an exact path plus theorem or function name,
and run `lean-proof-gate` on each Lean claim before it is cited as Tier A in this stream.

## 4. Status of the central theorem — must be settled first

In the published literature, universal optimality is **proved** in dimensions 8 (E8) and 24 (Leech),
by Cohn–Kumar–Miller–Radchenko–Viazovska (2022). For the **triangular lattice in dimension 2** it is
the well-known open **Cohn–Kumar conjecture** (Tier L: open). The brainstorm refers to an
"AI-generated, Lean-verified Cohn–Kumar planar theorem". Before anything in this stream is built on
it, review must establish exactly what the Lean artifact states:
- Is it the full universal-optimality statement among *all* periodic and non-periodic configurations?
- Or is it a restricted version, such as among lattices only (which relates to Montgomery 1988),
  among a finite family, under extra hypotheses, or a bound rather than optimality?
- Does it pass `lean-proof-gate`: build, no `sorry`, axioms ⊆ {`propext`, `Classical.choice`,
  `Quot.sound`}, statement lock, and producer ≠ verifier?

If the result is a full proof of the 2D conjecture, it is a major claim that needs independent
review before any external communication. If it is a restricted version, ideas 1, 2 and 5 must be
re-scoped to what is actually proved.

## 5. Review notes and risks (questions for the review pass)

**Idea 1 — benchmark**
- **Hardware model mismatch.** On AWS Braket, QuEra Aquila atoms sit at *fixed* tweezer positions
  and interact through Rydberg van der Waals C₆/r⁶ in the excited state. Atoms do not move
  continuously, and you cannot program a Yukawa potential. What is the encoding?
  - Candidate: a lattice-gas / maximum-independent-set formulation on a fine grid of candidate sites,
    where the Rydberg blockade radius sets the minimum spacing.
  - Pasqal (Pulser) has the same constraint.
- **Does the claim transfer to the grid?** The triangular optimum is a statement about the continuum.
  Does it carry over to the discretized site set? We need a theorem or an exact solve that fixes the
  ground state of the discretized problem.
- **D-Wave** is a discrete Ising/QUBO machine. It too needs a position discretization, and its
  embedding overhead may dominate.
- **What does "classically trapped" mean?** Simulated annealing and ODE gradient flow are weak
  baselines. Before claiming any advantage, compare against strong classical baselines:
  - parallel tempering;
  - basin hopping;
  - lattice-informed initialization;
  - exact solvers on the discretized problem.
- **Wording.** "Undeniable / certified advantage" is too strong. The certificate covers only the
  *known target state*, not the speed-up claim.

**Idea 2 — self-assembly**
- **Wrong regime for neutral atoms.** Ground-state neutral atoms do not repel, so passive
  self-assembly does not apply to Rydberg tweezer arrays. Tweezer positions are set optically.
- **Where self-assembly does apply.** 2D Penning-trap ion crystals (e.g. NIST, around 100+ ions) and
  electrons on helium form triangular Wigner crystals on their own.
- **"Flawless" needs a qualifier.** The theorem concerns infinite-lattice energy density. Finite
  crystals in a confining trap have curvature-induced defects and density gradients.
- **Is the "phononic stress" mechanism real?** Square tweezer arrays do not hold mutually repelling
  atoms, so the claimed stress needs a physical justification or should be dropped.
- **Positive:** the link to color codes on hexagonal/triangular lattices is real (Tier L).

**Idea 3 — vacancy qubits**
- **"Zero-cost" needs a qualifier.** "Same energy density" for one vacancy is a thermodynamic-limit
  statement. A vacancy still has a finite, non-zero formation energy.
- **Braiding statistics.** Are vacancies in a Wigner crystal anyons? Braiding gives topological
  protection only for non-abelian quasiparticles. What would make a vacancy one?

**Idea 4 — metal gates**
- **Scope.** Real gate geometries are patterned electrodes, not infinite parallel plates. Does the
  Poisson-summation result extend beyond the parallel-plate case?
- **"Exonerated" is too strong.** The result covers classical bulk energetics only. Gate disorder,
  patch potentials and finite-size effects remain possible causes of melting.

**Idea 5 — floor checks**
- **The principle holds.** For H = T + V with T ≥ 0, any quantum expectation value satisfies
  ⟨H⟩ ≥ min V. So a reported energy below the classical minimum is unphysical.
- **But the Lean bound is an infinite-lattice energy *density*.** A finite-N VQE run needs a
  finite-N lower bound, including boundary and trap terms. And the simulated Hamiltonian must
  match the bounded one exactly. Spin-model VQE (qubit Hamiltonians) does not inherit this floor
  automatically.
- **Is a new floor needed?** Existing noise mitigation already uses variational and N-representability
  bounds. What does a geometric floor add?

## 6. Proposed next step — idea #1 (to refine in review)

1. **Settle §4:** exact Lean statement, gate results, tier.
2. **Choose the encoding:** continuous → discretized site grid → Rydberg MIS / lattice-gas
   Hamiltonian. Prove or exactly solve the discretized ground state for small N.
3. **Check device constraints** (Aquila/Pasqal via Braket): maximum atom count, minimum spacing,
   geometry limits, Rabi/detuning ranges, shot budget.
4. **Build the classical baseline suite** in Rust, reusing rusty-SUNDIALS infrastructure:
   - simulated annealing;
   - parallel tempering;
   - basin hopping;
   - exact solve for small N.
   Record when each one is "trapped".
5. **Define the success metric:** probability of the target configuration versus wall-clock and
   energy budget. Run on the Braket local simulator first, then on the QPU.
6. **Add a Lean "floor" artifact:** a finite-N bound usable as a check in step 5.

## 7. Open questions for collaborators

- Neutral-atom experimentalists: can a lattice-gas encoding of a soft repulsive potential fit
  current blockade-radius and atom-count limits?
- Trapped-ion and e⁻-on-He groups: is the triangular-crystal guarantee useful for your layout or
  stability analysis, and what finite-size form would you need?
- Compiler engineers: where in a Qiskit/Cirq pipeline would a physics-derived energy floor plug in?

---

## 8. Update 2026-10-11 (project preparation): resolves §3–§5

Sections 2–7 above are left as written. This section records what the preparation pass found. Details are in
[DEPENDENCIES.md](DEPENDENCIES.md), [LITERATURE_REVIEW.md](LITERATURE_REVIEW.md) and
[QC_STREAM1_WORKFLOW.md](QC_STREAM1_WORKFLOW.md).

- **§4 central theorem.** The "Lean-verified Cohn–Kumar theorem" is `OAI.AtomicTriangular.universal_energy_minimum`
  in openai/math (`fd4aeeb2`). It is AI-generated, accepted by the kernel, and **not peer reviewed**. The 2D conjecture
  is still open in the peer literature (arXiv:2511.03353). SocrateAI's corollaries D1–D4 are in
  `~/triangular-universal-optimality-lean` (Zenodo 23285631, 23293429). Every Tier A claim here is therefore conditional.
- **§3 table, resolved:**
  - **Idea 1.** Evidence: YUK-TRI-1 in `rusty-SUNDIALS-wt-yukawa-global/crates/qf-yukawa-crystal`. At κ=1, annealing
    reached the lattice in 0/10 OC20 starts. Full-budget global runs are still owed, and an erratum on r_c is owed.
    Yukawa is only Tier C.
  - **Idea 2.** The Hessian saddle is `ctl_neg_square_saddle` in `results/controls.jsonl`, with 64–72 negative modes.
  - **Idea 3.** The "Vacancy Theorem" is D3: `universal_optimum_not_unique` and `vacancy_universally_optimal` in
    `UniversalOptimality.lean`. It holds in the liminf (lower-energy) sense.
  - **Idea 4.** The "fourth preprint" is *Gated exciton fluids I* (Zenodo 23294615, a paper proof). *Part II* (23297479)
    gives a 52-theorem Lean proof that the dual-gate image kernel is completely monotone. Its scope is the **exciton**
    kernel; the single-plane bare-charge case is a two-line Tier C argument (workflow P1.2).
  - **Idea 5.** `floor_check` and `check_reported_energy` are in `qf-yukawa-crystal/src/global_opt.rs`. They are
    one-sided and cover periodic geometry only.
- **Changes to the ideas:**
  - Idea 1 moves from Yukawa to **Riesz s = 6** (Rydberg C₆/r⁶, covered by D1). It becomes a *verification* benchmark
    on a site-occupation encoding, not an advantage claim.
  - Neutral-atom self-assembly (idea 2) and vacancy anyons (idea 3) are not supported by the theorem or the literature
    (findings F5, F7, F8).
  - Idea 4 is the strongest of the five.
