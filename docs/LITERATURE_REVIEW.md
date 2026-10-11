# QC Stream 1 — Literature review (first pass)

**Status (2026-10-11):** first pass, AI-assisted.
- 73 arXiv papers were selected; each id was checked against the real arXiv title.
- They are listed in `corpus/seed_papers.py` and indexed in Chroma collection `qc_literature`; see §5.
- No human has read these papers for this review yet. Each finding below gives its source id so that a reader can check it.

The six areas, called pillars below, match the brainstorm ideas: `foundation` (the shared mathematics), `benchmark` (1), `layout` (2), `defects` (3), `gates` (4), `floor` (5).

---

## 1. Findings that change the brainstorm

**F1. 2D Cohn–Kumar is still open in the peer literature.**
- CKMRV (1902.05438) proves universal optimality only for E8 and Leech.
- The strongest 2D results are weaker:
  - local optimality among all configurations for completely monotone potentials (Leblé et al., 2511.03353, Nov 2025);
  - optimality within restricted periodic classes (Hardin et al., 2307.15822);
  - optimality among lattices only (Montgomery 1988; Bétermin 1502.03839).
- The only global claim is the unreviewed AI proof in openai/math.

→ Every "certified ground state" in this stream is **conditional**. A benchmark that uses only lattice competitors, or small-unit-cell competitors, rests on proven results.

**F2. Petrache–Serfaty crystallization (1908.09714) is conditional on 2D Cohn–Kumar.** Do not cite it as an independent proof.

**F3. Triangular optimality fails outside the completely monotone class (1806.02233, 2104.09795).**
- Rydberg van der Waals C₆/r⁶ is completely monotone. It is Riesz s = 6, covered by D1.
- Rydberg *dressing* gives a soft-core plateau potential (1001.0519) that is **not** completely monotone.

→ Idea 1 must use bare C₆/r⁶, not dressing.

**F4. Quantum-advantage claims on these platforms are contested.**
- Rydberg MIS:
  - Ebadi 2022 (2202.09372) claimed a superlinear speedup.
  - Classical solvers handle instances at that scale easily (2307.09442).
  - Pasqal is still searching for hard native instances (2502.04291).
- D-Wave's beyond-classical claim (2403.00910) drew three rebuttals:
  - tensor networks (2503.05693);
  - neural quantum states (2607.08811);
  - variational Monte Carlo (2609.01719, not seeded).

→ Idea 1 needs Rønnow-style speedup methodology (1401.2910) and the strongest classical baselines. A "known ground state" helps only with *verification*, not with the advantage claim. Planted-solution benchmarks (1502.01663) are the closest precedent.

**F5. Neutral atoms do not offer continuous positions.**
- Tweezer positions are classical parameters set before the run (2306.11727, 2104.15044).
- Only small motion within a trap is quantum (2506.09865).

→ Idea 1 has to be encoded as occupation of candidate sites (Pichler 1808.10816). Floating-crystal phases on QuEra hardware (2401.08087) are the closest existing physics: incommensurate density-wave order on a fixed grid.

**F6. No paper emulates a true Yukawa potential on Rydberg arrays.** Screened Coulomb is native to trapped ions and to electrons near gates. Combined with Yukawa being only Tier C in Lean, this means **idea 1 should move from Yukawa κ=1 to Riesz s=6**. The κ=1 classical-trap evidence (YUK-TRI-1) then has to be re-established for s = 6.

**F7. Triangular Coulomb crystals already self-assemble in trapped-ion hardware.** Penning traps (1204.5789, 1512.03756) and 2D RF traps (2311.17163, 2302.00565) both form them.
- The confinement sets the lattice; nobody designs it.
- Coulomb (s = 1) is **not** covered by the Lean result.

→ Idea 2 should cite these as existing practice, and claim no new self-assembly for neutral atoms, which do not repel in their ground state. The real link to color codes on 3-colourable lattices is quant-ph/0605138, 2412.14256 and 2312.03982.

**F8. Vacancies in Wigner crystals are not anyons.**
- In fracton–elasticity duality (1711.11044, 2509.14344), point defects behave as fractons or dipoles: their mobility is restricted, but they have no braiding statistics.
- Non-Abelian braiding comes from twist defects or dislocations in topological codes (1004.1838, 1208.4834, 1204.0113, 1806.02820). Those are code-level objects.

→ Idea 3 needs to be rewritten. D3 says that a vacancy does not change the *liminf energy density*. It says nothing about formation energy, mobility or statistics.

**F9. Interstitials, not vacancies, have the lower formation energy in the 2D Wigner crystal** (QMC: cond-mat/0002366, 2206.07191). Near melting, defects self-dope and drive kinetic magnetism (2309.13121).

**F10. Gates screen the interaction and shift melting.**
- Metal or dielectric screening turns Coulomb dipolar beyond the gate distance and shifts melting (cond-mat/0411333).
- Gated TMD Wigner crystals are now imaged directly (2010.03078, 2106.10599, 2402.05456).
- Quantum melting occurs at r_s ≈ 31–37 (1002.2101; Tanatar–Ceperley 1989).

→ Idea 4's own work (Gated exciton fluids I/II) already lies in this line. Its negative Lindemann result (rigid exciton crystal needs d/a_M ≳ 49) belongs next to these papers.

**F11. Electron-on-neon/helium qubits use gate-defined single-electron traps** (2303.03688, 2106.10326, 2210.12337: about 0.1 ms coherence), not a self-assembled Wigner lattice.

→ Idea 4's "operating envelope" applies to many-electron crystal phases. It does not apply to the single-electron qubit architecture as currently designed.

**F12. Certified ground-state lower bounds are mature but hard to scale.** Approaches include SDP/RDM (1106.5275), renormalization-group bounds (2212.03014), certification (2310.05844, 2604.01555), entropy constraints (2305.06855), bootstrap (2006.06002) and Dual-VQE (2312.03083).
- Error mitigation can push estimates *below* the true ground energy (1612.02058, 2210.00921), which is the failure idea 5 targets.
- For Coulomb/jellium, the rigorous constant is the improved Lieb–Oxford bound (2203.12473). It lies far below the triangular Madelung energy.

→ Idea 5's geometric floor is a valid check only on Hamiltonians that are exactly a completely monotone pair potential over positions. It needs a finite-N version. Its value over SDP bounds is that it is closed-form and cheap.

## 2. Revised status of the five ideas

| # | Idea | Verdict after review | What survives |
|---|---|---|---|
| 1 | Certified benchmark | **Reframe** | A *verification* benchmark: Riesz-6 occupation problem on a site grid, with a target state proven only among lattice competitors (F1) and Rønnow-style controls (F4). This is not an advantage claim. |
| 2 | Triangular layouts | **Narrow** | Supports ion crystals (Coulomb, not covered) and color-code layouts. Drop neutral-atom self-assembly. |
| 3 | Vacancy qubits | **Rewrite or drop** | D3 as a statement about energy density. The qubit and braiding claims are unsupported (F8, F9). |
| 4 | Gate envelope | **Strongest** | Own Lean result (dual-gate CM kernel) plus a Tier C single-plane lemma. Scope: classical bulk energetics of crystal phases (F10, F11). |
| 5 | VQE floor | **Keep, as a narrow tool** | `check_reported_energy` port, finite-N bound required, placed alongside SDP bounds (F12). |

## 3. Papers not on arXiv (DOIs written from memory; **verify before citing**)

Montgomery 1988 (10.1017/S0017089500007047) · Rankin 1953 (10.1017/S2040618500035668) · Theil 2006
(10.1007/s00220-005-1458-7) · Bonsall–Maradudin 1977 (10.1103/PhysRevB.15.1959) · Platzman–Dykman 1999
(10.1126/science.284.5422.1967) · Tanatar–Ceperley 1989 (10.1103/PhysRevB.39.5005) · Grimes–Adams 1979
(10.1103/PhysRevLett.42.795) · Cockayne–Elser 1991 (10.1103/PhysRevB.43.623) · Halperin–Nelson 1978
(10.1103/PhysRevLett.41.121) · Lieb–Oxford 1981 (10.1002/qua.560190306) · Temple 1928 (10.1098/rspa.1928.0098).

## 4. Further candidate papers (verified ids, not yet seeded)

1603.06518, 1607.08716, 2411.17199, 1603.09684 (foundation) · 1512.02206, 1911.03446, 2202.05847, 2207.13800,
2609.01719, 2012.12281, 1707.04344, 2209.03965, 1602.06313 (benchmark) · cond-mat/0406600, cond-mat/0509436,
2005.12317, 1104.5047 (defects) · 2312.11632, 2210.15168, 2512.16050 (gates) · 2410.00810 (floor) · 1607.03044 (layout).

## 5. Vector DB

- Store: `~/AutoevolveAI/data/chroma`, shared with ANSE.
- Embeddings: Ollama `qwen3-embedding:0.6b`, 1024-d, cosine. The pipeline stops if Ollama is down rather than fall back to hash embeddings.
- Collections created for this stream:
  - `qc_literature`: arXiv papers (abstract plus up to 40 body chunks per paper). Built by `corpus/fetch_papers.py` then `corpus/ingest_chroma.py`; check with `corpus/query_chroma.py --verify`.
  - `qc_streams`: SocrateAI material from other streams and this repo. Every chunk is tagged `provenance: NOT peer-reviewed` with a `tier_note`. Built by `corpus/ingest_streams.py`.
- The existing collections (`adscmt_literature`, `adscmt_generated`, `phase1_traces`) are left untouched. A backup of the
  store made before the first write is at `~/AutoevolveAI/data/chroma_backups/chroma_pre_qc_2026-10-11`.
- LeanMaster's `.leancache/declarations.db` (a TF-IDF/SQLite index, not Chroma) was **not** re-indexed. It predates
  the D1–D3 corollaries; see workflow §5.

**Ingestion record (2026-10-11):**
- `qc_literature`: **2,574 chunks**, made of 73/73 abstracts plus 2,501 full-text body chunks (1024-d).
  `query_chroma.py --verify` **PASS 8/8** probes, both after the abstracts and after the full text.
- `qc_streams`: **91 chunks** from 21 documents. Each chunk is labelled with its real repository; worktree copies
  carry the branch name.
