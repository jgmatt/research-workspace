# Log: Attracting the Elite

---

## 2026-06-15 -- Codex cross-check and synthesized LaTeX writeup

**What happened:** Installed the Codex CLI (user npm prefix `~/.npm-global`; logged in via
ChatGPT) and delegated the same modeling task to a fresh Codex session (gpt-5.5, xhigh).
Codex wrote `model-codex.md` independently. Compared against my `model.md` and synthesized a
single definitive writeup `model.tex` (compiled to `model.pdf`, ~12pp).

**Codex cross-check caught three issues in my first draft (`model.md`):**
- The follower game is NOT a potential game under the asymmetry ($\alpha_{HL}\neq\alpha_{LH}$
  makes matrix $A$ asymmetric); my Lemma claiming a Rosenthal potential was wrong. Fixed:
  work directly with allocations + Wardrop inequalities.
- I dismissed the low-type invasion constraint (IC-L) too quickly. The correct lower bound is
  $B_K=(\alpha_{HH}-\alpha_{LH})m_H/K$, and crucially a *small* $\alpha_{LH}$ (the asymmetry)
  *raises* $B_K$, making the poor *harder* to keep out of premium resorts. So one-way aversion
  helps via $\alpha_{HL}$ but hurts via the IC-L channel; feasibility needs $A_K\ge B_K$.
- I omitted the pooling rent. Correct profit identity: $\Pi^S(K)-\Pi^P=\Delta W(K)+T^P-R_K$,
  with screening rent $R_K=m_H(d-A_K)_+ + m_L(B_K-d)_+$.

**Cleanest new results (now in model.tex):** generalized-price sandwich
$B_K\le q_H-q_L\le A_K$; optimal split $K^\star/J=\sqrt{\alpha_{HH}}m_H/(\sqrt{\alpha_{HH}}m_H+\sqrt{\alpha_{LL}}m_L)$;
at the optimum, sorting raises *surplus* iff $\alpha_{HL}+\alpha_{LH}>2\sqrt{\alpha_{HH}\alpha_{LL}}$,
and the *same* product governs local stability of pooling
($\alpha_{HH}\alpha_{LL}>\alpha_{HL}\alpha_{LH}$) -- under near one-way aversion pooling stays
stable however large $\alpha_{HL}$ is, a sharp wrong-equilibrium trap.

**Artifacts:** `model.md` (Claude v1), `model-codex.md` (Codex independent), `model.tex` +
`model.pdf` (synthesis). Codex session UUID recorded in project `CLAUDE.md` under `## Codex`.

**Next step:** Decide whether to push the non-collusive (competitive) pricing game as the
headline result; formalize the capacity instrument repairing $A_K<B_K$; pin down basin of
attraction for the trap.

---

## 2026-06-15 -- First formal model: coordinated sorting under asymmetric peer congestion

**What happened:** Wrote `model.md`, a self-contained model note answering the cartel
question directly: J identical resorts, two tourist types (rich H, poor L) with linear
composition-dependent congestion and the asymmetry $\alpha_{HL} \gg \alpha_{LH}$ (rich
dislike poor crowding, poor are indifferent). Characterized (i) the tourist Wardrop
equilibrium given prices, (ii) the symmetric pooling baseline, (iii) the coordinated
separating regime (premium H-only vs budget L-only resorts).

**Key results:**
- Segregation strips the cross-congestion term $\alpha_{HL} m_L/J$ out of the rich type's
  cost; since the poor are indifferent, that relief is pure surplus the cartel sells back.
- The asymmetry has a *dual role*: it is the screening device. (IC-H) reads
  $(\alpha_{HL}-\alpha_{LL})\,m_L/J_L \ge v_H - v_L$ -- the rich self-select into the
  premium tier without an information rent precisely when their distaste for the poor is
  strong relative to the value gap. When it fails, the cartel leaves a rent $R$.
- Sorting-dominance proposition: $\Pi^{\text{sort}} > \Pi^{\text{pool}}$ iff the
  value-discrimination gain $(v_H-v_L)m_H$ (plus the poor-externality term if
  $\alpha_{LH}>0$) exceeds the own-type concentration cost. Optimal premium share
  $J_H^\star/J = \sqrt{\alpha_{HH}}\,m_H / (\sqrt{\alpha_{HH}}\,m_H + \sqrt{\alpha_{LL}}\,m_L)$.
- Discussed breakers: aspirational poor ($\alpha_{LH}<0$ flips a term against sorting),
  (IC-L) invasion / wrong-equilibrium trap repaired by a capacity instrument, and
  collusion-vs-competition (asymmetric congestion is self-limiting under competition too).

**Note:** Intended to delegate the same task to Codex in parallel, but the Codex CLI is not
installed on this machine (`command not found`); delegation skipped.

**Next step:** Pressure-test the proposition (sign/derivation check), add the capacity
instrument formally, and decide whether to push the competition (non-collusive) version as
the cleaner publishable result.

---

## 2026-06-15 -- Literature mapping and research question refinement

**What happened:** Mapped the existing literature to locate the precise gap. Key finding: congestion games (Rosenthal 1973, Sandholm 2010) reduce the externality to scalar load or aggregate mass; club-good models (Buchanan 1965, Scotchmer 1994) capture composition preferences but are static and non-strategic on the destination side; Schelling (1971) has composition thresholds but no strategic destinations. None combine composition-dependent payoffs $u_i(n^H_\ell, n^L_\ell)$ with asymmetric cross-type derivatives and a strategic destination layer.

**Key decisions:**
- The novel theoretical core is a two-destination, two-type congestion game with composition-dependent payoffs and strategic destination pricing -- proving when a separating equilibrium exists and what breaks it.
- Closest anchors to build from: Milchtaich (1996) for player-specific congestion, Sandholm (2010) for the population game framework, Scotchmer (2002) for composition-in-clubs.
- Butler's TALC lifecycle is the empirical phenomenon to formalize; Venice, Santorini, Bhutan are natural empirical targets.

**Refined research question:** How to design price and amenity instruments for a destination competing for two tourist types under composition-dependent payoffs $u_i(n^H_\ell, n^L_\ell)$, such that a separating equilibrium exists and is stable against low-type invasion?

**Next step:** Run targeted literature search to catch recent work on composition-dependent congestion games; sketch the formal model (equilibrium characterization + screening problem).

---

## 2026-06-15 -- Project kickoff and brainstorming

**What happened:** Initial brainstorming session on population games and tourism. Identified the core setup: heterogeneous tourist types with different congestion sensitivities, destinations as strategic agents choosing instruments in a Stackelberg game over the tourist population equilibrium.

**Key decisions:**
- Frame as a population game (not a static game) to capture dynamics of how tourist type-distributions shift over time.
- Composition-dependent payoffs (not just count-dependent) are the distinguishing structural feature.
- The "wrong equilibrium trap" is the central phenomenon to explain and solve.

**Next step:** Targeted literature search to confirm gaps in (1) heterogeneous-type congestion games and (2) mechanism design over population game equilibria in tourism contexts.
