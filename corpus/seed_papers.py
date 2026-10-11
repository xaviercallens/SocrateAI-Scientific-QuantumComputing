"""Seed corpus for the QC Stream 1 literature review (2026-10-11).

Each entry is (arxiv_id, pillar, expected_title_fragment). `fetch_papers.py`
refuses any record whose real arXiv title does not contain the fragment, so a
mistyped identifier fails loudly instead of ingesting the wrong paper.

Pillars follow the five brainstorm ideas plus their mathematical base:
  foundation - Cohn-Kumar universal optimality, 2D crystallization, Coulomb/Riesz gases
  benchmark  - idea 1: annealing / Rydberg-MIS advantage claims and their critiques
  layout     - idea 2: 2D ion crystals, tweezer geometries, color codes
  defects    - idea 3: Wigner-crystal point defects, fractons, twist-defect braiding
  gates      - idea 4: electrons on helium/neon, gated and moire Wigner crystals, melting
  floor      - idea 5: certified ground-state lower bounds, VQE error mitigation
"""

SEED_PAPERS: list[tuple[str, str, str]] = [
    # --- foundation ---------------------------------------------------------
    ("math/0607446", "foundation", "universally optimal distribution of points on spheres"),
    ("1902.05438", "foundation", "leech lattices and interpolation formulas"),
    ("1603.04246", "foundation", "the sphere packing problem in dimension 8"),
    ("1908.09714", "foundation", "crystallization for coulomb and riesz interactions"),
    ("2511.03353", "foundation", "the hexagonal lattice is universally locally optimal"),
    ("2307.15822", "foundation", "universally optimal periodic configurations in the plane"),
    ("1502.03839", "foundation", "2d theta functions and crystallization among bravais lattices"),
    ("1806.02233", "foundation", "optimal and non-optimal lattices for non-completely monotone"),
    ("2104.09795", "foundation", "optimality of the triangular lattice for lennard-jones"),
    ("1504.01153", "foundation", "the crystallization conjecture: a review"),
    ("1201.3503", "foundation", "2d coulomb gases and the renormalized energy"),
    ("2202.09240", "foundation", "coulomb and riesz gases: the known and the unknown"),
    ("1603.05202", "foundation", "packing, coding, and ground states"),
    # --- benchmark (idea 1) ------------------------------------------------
    ("1401.2910", "benchmark", "defining and detecting quantum speedup"),
    ("1304.4595", "benchmark", "quantum annealing with more than one hundred qubits"),
    ("1705.07452", "benchmark", "scaling advantage for a quantum annealer over simulated annealing"),
    ("1502.01663", "benchmark", "spin glass problems with planted solutions"),
    ("2403.00910", "benchmark", "beyond-classical computation in quantum simulation"),
    ("2503.05693", "benchmark", "dynamics of disordered quantum systems with two- and three-dimensional tensor networks"),
    ("2607.08811", "benchmark", "comment on \"beyond-classical computation in quantum simulation\""),
    ("2202.09372", "benchmark", "quantum optimization of maximum independent set using rydberg atom arrays"),
    ("1808.10816", "benchmark", "quantum optimization for maximum independent set using rydberg atom arrays"),
    ("2307.09442", "benchmark", "hardness of the maximum independent set problem on unit-disk graphs"),
    ("2502.04291", "benchmark", "identifying hard native instances for the maximum independent set"),
    ("2306.11727", "benchmark", "aquila: quera's 256-qubit neutral-atom quantum computer"),
    ("2104.15044", "benchmark", "pulser: an open-source package for the design of pulse sequences"),
    ("2401.08087", "benchmark", "probing quantum floating phases in rydberg atom arrays"),
    ("2002.04987", "benchmark", "critical energy landscape of linear soft spheres"),
    ("1001.0519", "benchmark", "rydberg"),
    # --- layout (idea 2) ---------------------------------------------------
    ("1512.03756", "layout", "quantum spin dynamics and entanglement generation with hundreds of trapped ions"),
    ("1204.5789", "layout", "engineered 2d ising interactions on a trapped-ion quantum simulator"),
    ("2311.17163", "layout", "a site-resolved 2d quantum simulator with hundreds of trapped ions"),
    ("2302.00565", "layout", "controlling two-dimensional coulomb crystals of more than 100 ions"),
    ("quant-ph/0605138", "layout", "topological quantum distillation"),
    ("2412.14256", "layout", "scaling and logic in the color code on a superconducting quantum processor"),
    ("1607.03042", "layout", "an atom-by-atom assembler of defect-free arbitrary 2d atomic arrays"),
    ("2403.12021", "layout", "a tweezer array with 6100 highly coherent atomic qubits"),
    ("2312.03982", "layout", "logical quantum processor based on reconfigurable atom arrays"),
    ("2012.12268", "layout", "programmable quantum simulation of 2d antiferromagnets with hundreds of rydberg atoms"),
    ("2506.09865", "layout", "rydberg atom arrays as quantum simulators for molecular dynamics"),
    # --- defects (idea 3) --------------------------------------------------
    ("cond-mat/0002366", "defects", "single and paired point defects in a 2d wigner crystal"),
    ("2206.07191", "defects", "interstitial-induced ferromagnetism in a two-dimensional wigner crystal"),
    ("2309.13121", "defects", "dynamical defects in a two-dimensional wigner crystal"),
    ("2509.14344", "defects", "defects in wigner crystals: fracton-elasticity duality and vacancy proliferation"),
    ("2607.18477", "defects", "theory of two-dimensional wigner crystals with defects"),
    ("1711.11044", "defects", "fracton-elasticity duality"),
    ("1004.1838", "defects", "topological order with a twist: ising anyons from an abelian model"),
    ("1208.4834", "defects", "genons, twist defects, and projective non-abelian braiding statistics"),
    ("1204.0113", "defects", "projective non-abelian statistics of dislocation defects"),
    ("1806.02820", "defects", "the boundaries and twist defects of the color code"),
    # --- gates (idea 4) ----------------------------------------------------
    ("quant-ph/0007113", "gates", "quantum computing using electrons floating on liquid helium"),
    ("0912.1406", "gates", "trapped electrons on helium using cavity quantum electrodynamics"),
    ("2106.10326", "gates", "single electrons on solid neon as a solid-state qubit platform"),
    ("2210.12337", "gates", "electron charge qubits with 0.1 millisecond coherence time"),
    ("2303.03688", "gates", "blueprint for quantum computing using electrons on helium"),
    ("cond-mat/0411333", "gates", "melting temperature of screened wigner crystal on helium films"),
    ("2010.03078", "gates", "observation of wigner crystal of electrons in a monolayer semiconductor"),
    ("2010.03037", "gates", "signatures of bilayer wigner crystals"),
    ("1910.09047", "gates", "mott and generalized wigner crystal states"),
    ("2106.10599", "gates", "imaging generalized wigner crystal states"),
    ("2402.05456", "gates", "quantum melting of a disordered wigner solid"),
    ("1002.2101", "gates", "phase diagram of the low-density two-dimensional homogeneous electron gas"),
    ("0905.4515", "gates", "hexatic and mesoscopic phases in the 2d quantum coulomb system"),
    # --- floor (idea 5) ----------------------------------------------------
    ("1106.5275", "floor", "lower bounds for ground states of condensed matter systems"),
    ("2212.03014", "floor", "lower bounding ground-state energies of local hamiltonians"),
    ("2310.05844", "floor", "certifying ground-state properties of quantum many-body systems"),
    ("2604.01555", "floor", "scalable ground-state certification of quantum spin systems"),
    ("2305.06855", "floor", "entropy constraints for ground energy optimization"),
    ("2006.06002", "floor", "quantum many-body bootstrap"),
    ("2312.03083", "floor", "dual-vqe: a quantum algorithm to lower bound the ground-state energy"),
    ("2210.00921", "floor", "quantum error mitigation"),
    ("1612.02058", "floor", "error mitigation for short-depth quantum circuits"),
    ("2203.12473", "floor", "improved lieb-oxford bound on the indirect and exchange energies"),
]
