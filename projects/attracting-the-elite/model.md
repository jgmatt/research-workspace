# A Model of Coordinated Sorting under Asymmetric Peer Congestion

This note develops a rigorous model of the following question. Several **identical**
resorts (no intrinsic quality differences) face a heterogeneous tourist population.
Starting from a symmetric baseline where every resort sets the same price, can the
resorts raise their **total** profit by **coordinating on differentiated prices** that
split the population by type, one resort going cheap to absorb the poor, another going
expensive to capture the rich? The mechanism that makes this work is an **asymmetric
peer externality**: rich tourists dislike being crowded by poor tourists, but poor
tourists do not mind the rich.

The short answer: yes, and the asymmetry is exactly what makes sorting both *feasible*
(tourists self-select) and *profitable* (the cartel extracts the congestion relief as
surplus). Below I build the model, characterize both regimes, and give the parameter
condition under which sorting strictly dominates.

---

## 1. Primitives

**Tourists.** A continuum (nonatomic population game). Two types:

- High type $H$ ("rich"): mass $m_H$, gross value (budget / willingness-to-pay) $v_H$.
- Low type $L$ ("poor"): mass $m_L$, gross value $v_L$, with $v_H > v_L > 0$.

Let $\theta \in \{H, L\}$ index type. Each tourist chooses one resort to visit (or the
outside option, normalized to utility $0$).

**Resorts.** $J \ge 2$ resorts, indexed $j = 1, \dots, J$, *intrinsically identical*.
Resort $j$ posts a price $p_j \ge 0$. Marginal cost of service is normalized to $0$
(adding a constant marginal cost $c$ rescales nothing essential). The population state at
resort $j$ is the pair $\big(n^H_j, n^L_j\big)$ of masses of each type present.

**Payoffs.** A type-$\theta$ tourist at resort $j$ receives

$$
u_\theta(j) \;=\; v_\theta \;-\; p_j \;-\; C_\theta\!\big(n^H_j, n^L_j\big),
$$

where $C_\theta$ is the congestion / peer cost. I take it linear:

$$
C_H\big(n^H, n^L\big) = \alpha_{HH}\, n^H + \alpha_{HL}\, n^L, \qquad
C_L\big(n^H, n^L\big) = \alpha_{LH}\, n^H + \alpha_{LL}\, n^L.
$$

So the cross-congestion matrix is

$$
A = \begin{pmatrix} \alpha_{HH} & \alpha_{HL} \\ \alpha_{LH} & \alpha_{LL} \end{pmatrix}, \qquad \alpha_{\theta\theta'} \ge 0 .
$$

**The asymmetry (key assumption).** Rich dislike being crowded by poor much more than the
reverse:

$$
\boxed{\;\alpha_{HL} \;\gg\; \alpha_{LH}\;}
$$

The clean benchmark is the *one-directional* externality $\alpha_{LH} = 0$: the poor are
indifferent to the presence of the rich. (Section 6 treats $\alpha_{LH} > 0$ and the
"aspirational" case $\alpha_{LH} < 0$.) The own-type terms $\alpha_{HH}, \alpha_{LL} > 0$
represent ordinary physical crowding (lift lines, restaurant queues) and prevent everyone
from piling into a single resort.

---

## 2. Tourist equilibrium given prices (the population game)

Fix a price profile $\mathbf{p} = (p_1, \dots, p_J)$. A **tourist (Wardrop / Nash)
equilibrium** is an allocation $\{(n^H_j, n^L_j)\}_{j}$ with $\sum_j n^\theta_j \le m_\theta$
such that each type uses only resorts that maximize its utility, and uses the outside
option only if no resort gives positive utility. Formally, define the equilibrium utility
of type $\theta$:

$$
U_\theta^\star \;=\; \max\Big\{\,0,\; \max_{j} \big[\, v_\theta - p_j - C_\theta(n^H_j, n^L_j)\,\big]\Big\}.
$$

Then for each type $\theta$ and resort $j$:

$$
n^\theta_j > 0 \;\Longrightarrow\; v_\theta - p_j - C_\theta(n^H_j, n^L_j) = U_\theta^\star,
\qquad
v_\theta - p_j - C_\theta(n^H_j, n^L_j) \le U_\theta^\star \;\;\forall j .
$$

Because $C_\theta$ is linear (hence the game is a *potential game* in the sense of
Sandholm 2010 / Rosenthal 1973, with composition-dependent costs), an equilibrium exists;
with strictly positive own-congestion $\alpha_{\theta\theta} > 0$ the type-allocation is
generically unique on the set of used resorts. This is the **follower** problem; the
resorts are the **leaders** (Stackelberg).

---

## 3. Baseline regime: symmetric pricing (pooling)

Suppose all resorts post the same price $p_j = p$. By symmetry there is an equilibrium in
which each type spreads evenly:

$$
n^H_j = \frac{m_H}{J}, \qquad n^L_j = \frac{m_L}{J} \quad \text{for all } j .
$$

Every resort is **mixed**: rich and poor share each mountain. The net (congestion-adjusted)
willingness-to-pay of each type at a representative resort is

$$
w_H^{\text{pool}} = v_H - \alpha_{HH}\frac{m_H}{J} - \alpha_{HL}\frac{m_L}{J}, \qquad
w_L^{\text{pool}} = v_L - \alpha_{LH}\frac{m_H}{J} - \alpha_{LL}\frac{m_L}{J}.
$$

A single posted price cannot discriminate, so the colluding resorts (a joint
profit-maximizer) face the textbook monopoly choice between **serving everyone** at the
lower net WTP and **serving only the rich** at their net WTP:

$$
\Pi^{\text{pool}} \;=\; \max\Big\{\,
\underbrace{w_L^{\text{pool}} \,(m_H + m_L)}_{\text{serve all at } p = w_L^{\text{pool}}},\;\;
\underbrace{w_H^{\text{pool}} \, m_H}_{\text{serve only }H \text{ at } p = w_H^{\text{pool}}}
\,\Big\}.
$$

(The first term requires $w_L^{\text{pool}} \le w_H^{\text{pool}}$ for the rich to stay,
which holds whenever the value gap $v_H - v_L$ is not dwarfed by congestion differences;
assume it.) The defining inefficiency of this regime: **the rich pay the congestion cost
$\alpha_{HL} m_L / J$ of mixing with the poor, and the cartel cannot charge anyone for
relieving it**, because with identical prices it cannot separate the types.

---

## 4. Sorted regime: coordinated differentiation (screening)

Now let the resorts **coordinate**. Designate $J_H$ resorts as *premium* (intended for $H$)
and $J_L = J - J_H$ as *budget* (intended for $L$), posting prices $p_H$ and $p_L$
respectively. Conjecture a **separating** equilibrium: all $H$ at premium resorts, all $L$
at budget resorts, evenly split within each tier:

$$
\text{premium: } n^H = \frac{m_H}{J_H},\; n^L = 0; \qquad
\text{budget: } n^H = 0,\; n^L = \frac{m_L}{J_L}.
$$

Net WTP in each (now single-type) tier:

$$
w_H^{\text{sort}} = v_H - \alpha_{HH}\frac{m_H}{J_H}, \qquad
w_L^{\text{sort}} = v_L - \alpha_{LL}\frac{m_L}{J_L}.
$$

Note $w_H^{\text{sort}} > w_H^{\text{pool}}$: **segregation strips the cross-congestion term
$\alpha_{HL} m_L/J$ out of the rich type's cost**. That recovered surplus is what the cartel
will sell back.

### 4.1 Constraints for the separating equilibrium to hold

The cartel can set $p_H = w_H^{\text{sort}}$ and $p_L = w_L^{\text{sort}}$ (full extraction,
$U_H^\star = U_L^\star = 0$) **only if** no type wants to deviate to the other tier. The
relevant constraints:

**(IR)** Participation: $p_H = w_H^{\text{sort}} \ge 0$ and $p_L = w_L^{\text{sort}} \ge 0$.

**(IC-L)** The poor must not invade premium resorts. If an $L$ deviates to a premium resort
(price $p_H$, currently rich-only) it gets $v_L - p_H - \alpha_{LH} \frac{m_H}{J_H}$ (the
deviation is infinitesimal, so the resort's composition is unchanged). Non-deviation
requires

$$
v_L - p_H - \alpha_{LH}\frac{m_H}{J_H} \;\le\; 0
\;\;\Longleftrightarrow\;\;
p_H \;\ge\; v_L - \alpha_{LH}\frac{m_H}{J_H}.
$$

Since $p_H = w_H^{\text{sort}} = v_H - \alpha_{HH} m_H/J_H$ and $v_H > v_L$, this holds
easily: **the high price screens out the poor.** (Standard: the low type is excluded by price.)

**(IC-H)** The rich must not slum it at a budget resort. If an $H$ deviates to a budget
resort (price $p_L$, crowded with poor) it gets
$v_H - p_L - \alpha_{HL} \frac{m_L}{J_L}$. Non-deviation requires

$$
v_H - p_L - \alpha_{HL}\frac{m_L}{J_L} \;\le\; \underbrace{U_H^\star}_{=\,0}
\;\;\Longleftrightarrow\;\;
\alpha_{HL}\frac{m_L}{J_L} \;\ge\; v_H - p_L .
$$

Substituting $p_L = w_L^{\text{sort}} = v_L - \alpha_{LL} m_L/J_L$:

$$
\boxed{\;\big(\alpha_{HL} - \alpha_{LL}\big)\,\frac{m_L}{J_L} \;\ge\; v_H - v_L\;}
\tag{IC-H}
$$

This is the crux. **The rich type's incentive constraint is relaxed precisely by the
asymmetric congestion $\alpha_{HL}$.** The distaste the rich feel for the poor is what keeps
them from chasing the cheap budget price; it is the cartel's screening device. If
$\alpha_{HL}$ is large enough relative to the value gap $v_H - v_L$, (IC-H) holds and the
cartel achieves **full surplus extraction** from both types.

### 4.2 When (IC-H) binds: information rent

If $\alpha_{HL}$ is not large enough, (IC-H) fails at full extraction and the cartel must
leave the rich an **information rent**: lower $p_H$ until the rich are indifferent between
the premium tier and slumming. Setting the deviation payoff equal:

$$
v_H - p_H - \alpha_{HH}\tfrac{m_H}{J_H} \;=\; v_H - p_L - \alpha_{HL}\tfrac{m_L}{J_L}
\;\Longrightarrow\;
p_H = w_H^{\text{sort}} - \underbrace{\Big[(v_H - v_L) - (\alpha_{HL}-\alpha_{LL})\tfrac{m_L}{J_L}\Big]^+}_{\text{rent }R}.
$$

The rent $R$ shrinks as $\alpha_{HL}$ rises and vanishes when (IC-H) holds. This is the
familiar screening trade-off (à la Mussa–Rosen / Maskin–Riley), but here the
"quality" the rich are paying for is **endogenous exclusivity** rather than an exogenous
product attribute.

### 4.3 Cartel profit under sorting

$$
\Pi^{\text{sort}}(J_H) \;=\; p_H\, m_H + p_L\, m_L
\;=\; \Big(w_H^{\text{sort}} - R\Big) m_H + w_L^{\text{sort}}\, m_L .
$$

---

## 5. Main result: when does sorting beat pooling?

Take the clean case where (IC-H) holds (large asymmetry, so $R = 0$), and compare with the
pooling regime in its "serve all" form. Using
$w_H^{\text{sort}} = v_H - \alpha_{HH} m_H/J_H$ and
$w_L^{\text{sort}} = v_L - \alpha_{LL} m_L/J_L$:

$$
\Pi^{\text{sort}} = \Big(v_H - \alpha_{HH}\tfrac{m_H}{J_H}\Big) m_H + \Big(v_L - \alpha_{LL}\tfrac{m_L}{J_L}\Big) m_L,
$$

$$
\Pi^{\text{pool}} = \Big(v_L - \alpha_{LH}\tfrac{m_H}{J} - \alpha_{LL}\tfrac{m_L}{J}\Big)(m_H + m_L).
$$

> **Proposition (sorting dominance).** Suppose (IC-H), (IC-L), (IR) hold. Then coordinated
> sorting strictly increases total profit, $\Pi^{\text{sort}} > \Pi^{\text{pool}}$, if and
> only if
>
> $$
> \underbrace{(v_H - v_L)\, m_H}_{\substack{\text{(i) price-discrimination gain:}\\ \text{rich now pay near } v_H,\ \text{not } v_L}}
> \;+\;
> \underbrace{\alpha_{LH}\frac{m_H(m_H+m_L)}{J}}_{\substack{\text{(ii) externality the poor}\\ \text{no longer impose, if }\alpha_{LH}>0}}
> \;>\;
> \underbrace{\alpha_{HH} m_H\!\Big(\tfrac{m_H}{J_H} - \tfrac{m_H}{J}\Big) + \alpha_{LL} m_L\!\Big(\tfrac{m_L}{J_L} - \tfrac{m_L}{J}\Big)}_{\substack{\text{(iii) own-type concentration cost:}\\ \text{packing each type into fewer resorts}}}.
> $$

**Reading it.** Sorting wins when the **value gap** $v_H - v_L$ is large (lots of rich
surplus to extract once you can price-discriminate) and the **own-type congestion**
$\alpha_{HH}, \alpha_{LL}$ is modest (concentrating each type is cheap). The asymmetric
cross term $\alpha_{HL}$ does *not* appear on the benefit side of this particular
inequality directly — instead it works **through the constraint (IC-H)**: it is what makes
the full-extraction prices *attainable* in the first place. Without enough $\alpha_{HL}$,
$R > 0$ and the price-discrimination gain (i) is eroded by the information rent. So the
asymmetry plays a dual role:

1. **Feasibility:** $\alpha_{HL}$ large $\Rightarrow$ (IC-H) slack $\Rightarrow$ the rich
   self-select into the premium tier without a rent. The distaste *is* the sorting device.
2. **Surplus source:** segregation removes $\alpha_{HL} m_L/J$ from the rich type's cost,
   and because the poor are indifferent ($\alpha_{LH}\approx 0$) **no one is made worse off
   by the move** — the relief is pure surplus the cartel converts to price.

### 5.1 Optimal number of premium resorts

Treating $J_H$ as continuous and minimizing total own-congestion
$\alpha_{HH} m_H^2/J_H + \alpha_{LL} m_L^2/(J - J_H)$ over $J_H \in (0, J)$ gives the
interior optimum

$$
\boxed{\;\frac{J_H^\star}{J_L^\star} \;=\; \sqrt{\frac{\alpha_{HH}}{\alpha_{LL}}}\;\cdot\;\frac{m_H}{m_L}
\quad\Longrightarrow\quad
J_H^\star = J\cdot\frac{\sqrt{\alpha_{HH}}\,m_H}{\sqrt{\alpha_{HH}}\,m_H + \sqrt{\alpha_{LL}}\,m_L}\;}
$$

So the cartel allocates *capacity* (number of resorts) across tiers in proportion to each
type's mass weighted by the square root of its own-congestion sensitivity. A small, very
crowd-averse rich segment still gets its own resort(s); the rest serve the mass market.
(Integer constraints then round $J_H^\star$.)

---

## 6. What breaks it, and variations

- **Symmetric externality ($\alpha_{HL} = \alpha_{LH}$).** Sorting still removes
  cross-congestion, but now the *poor also* dislike the rich, so segregation benefits both
  and the welfare story is symmetric. The profit comparison still favors sorting when the
  value gap is large, but (IC-H) is governed by $\alpha_{HL} - \alpha_{LL}$ exactly as
  before — the *level* of $\alpha_{HL}$ still does the screening. The asymmetry is not
  required for profitability; it is what makes the welfare incidence one-sided (only the
  rich were ever hurt by mixing).

- **Aspirational poor ($\alpha_{LH} < 0$).** If the poor *enjoy* proximity to the rich,
  segregation *hurts* the poor: $w_L^{\text{sort}} = v_L - \alpha_{LL} m_L/J_L$ loses the
  positive term $-\alpha_{LH} m_H/J$ they had under pooling, so $p_L$ falls and term (ii)
  in the Proposition flips sign against sorting. Now there is genuine tension: the cartel
  trades off rich-extraction against the lost willingness-to-pay of star-struck poor. This
  is the empirically interesting case (clubs, nightlife, "see and be seen" destinations).

- **(IC-L) can bind too** if premium resorts are *underpriced* relative to the poor's value
  (e.g. when $\alpha_{HH}$ is huge so $p_H$ is driven low). Then the poor invade the premium
  tier and the separating equilibrium collapses into pooling — a **"wrong equilibrium
  trap"**: the resort meant to be exclusive gets swamped, the rich flee, and the cartel is
  back to $\Pi^{\text{pool}}$. Capacity caps $k_j$ (a second instrument) restore separation
  by physically rationing the premium tier.

- **Competition vs. collusion.** Everything above is the *joint* (cartel / single
  multi-resort owner) problem. Under price *competition* between independently owned
  resorts, the separating configuration is an equilibrium only if no single resort gains by
  re-pricing to poach the other tier; the asymmetric congestion again helps, because a
  premium resort that cuts price to attract volume immediately imports the cross-congestion
  that repels its rich clientele. This self-limiting force is what can sustain
  differentiation *without* explicit collusion — a separate result worth formalizing.

- **Dynamics / equilibrium selection.** Under replicator or BNN dynamics on the type-by-resort
  allocation, the separating state is locally stable exactly when (IC-H) and (IC-L) hold as
  *strict* inequalities (no type has a profitable infinitesimal migration). The pooling and
  separating equilibria can coexist as stable rest points with a basin boundary — formalizing
  the "trap" and explaining why a destination that *starts* mass-market struggles to climb to
  the exclusive equilibrium without a coordinated policy jump (price + capacity) to cross the
  basin boundary.

---

## 7. One-paragraph summary

Identical resorts, a heterogeneous population, and an asymmetric peer externality
($\alpha_{HL} \gg \alpha_{LH}$) are enough to make **coordinated price-differentiation strictly
more profitable than symmetric pricing**. Segregation removes the congestion the rich suffer
from the poor; because the poor are indifferent, that relief is pure surplus, and the cartel
captures it by charging the rich a near-full-value premium price. The asymmetry's deeper role
is as a **screening technology**: the rich type's distaste for the poor (the term
$(\alpha_{HL} - \alpha_{LL})\, m_L/J_L$) is exactly what discourages them from chasing the cheap
budget price, so the separating menu is incentive-compatible without leaving an information
rent. Sorting dominates when the value gap is large and own-type crowding is mild; it is
defeated by strong own-congestion, aspirational poor, or an under-capacitated premium tier that
the poor can invade (the wrong-equilibrium trap), which a capacity instrument repairs.
