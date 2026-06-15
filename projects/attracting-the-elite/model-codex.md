# Coordinated Sorting by Identical Resorts Under Asymmetric Peer Congestion

## 1. Purpose and modeling choice

This note studies whether a cartel of ex ante identical resorts can earn more by
choosing different posted prices and inducing tourists to sort by type than by
choosing one common price and serving a pooled tourist population.

The main closed-form comparison is between full-market-coverage regimes: all
members of both tourist populations visit in both the pooling and sorting
branches. This restriction isolates the value of sorting from the separate
question of optimal exclusion or quantity restriction. Section 8 explains how
to extend the comparison when the cartel may induce partial participation.

The important restrictions are:

1. Resorts have no intrinsic quality differences.
2. Tourist type is private, so a resort cannot directly charge a type-contingent
   price.
3. Each resort posts one admission price. Any tourist may choose any resort.
4. Sorting must therefore be self-enforcing through tourist choice.
5. Peer effects depend on the composition of visitors. In particular, high types
   may dislike low types much more than low types dislike high types.

The model distinguishes two gains from coordinated sorting. First, sorting can
raise total surplus by removing costly cross-type contact. Second, sorting can
implement second-degree price discrimination and recover rents that a common
pooling price must leave to one type. Sorting can also be costly because each
type is concentrated in fewer resorts.

## 2. Primitives

There are \(J \geq 2\) ex ante identical resorts, indexed by
\(j \in \mathcal J=\{1,\ldots,J\}\). There are two nonatomic tourist populations,
\(t \in \{H,L\}\), with masses \(m_H>0\) and \(m_L>0\). Let
\(M=m_H+m_L\).

A type-\(t\) tourist obtains gross value \(v_t\) from a resort visit, where

$$
v_H \geq v_L>0.
$$

The outside option gives utility zero. The gross values can be interpreted as
willingness to pay. A separate hard budget constraint can be added, but is not
needed for the main result.

**Maintained market-coverage assumption.** In the two principal regimes, prices
are required to satisfy participation for the full masses \(m_H\) and \(m_L\).
The cartel may be able to earn still more by excluding a type or inducing
partial participation. Such policies are distinct benchmark branches and must
be checked before making a claim about the unrestricted global optimum.

Let \(x_{tj}\geq 0\) be the mass of type \(t\) at resort \(j\). Peer congestion is
linear:

$$
\begin{pmatrix}
c_H(x_{Hj},x_{Lj})\\
c_L(x_{Hj},x_{Lj})
\end{pmatrix}
=
\begin{pmatrix}
\alpha_{HH} & \alpha_{HL}\\
\alpha_{LH} & \alpha_{LL}
\end{pmatrix}
\begin{pmatrix}
x_{Hj}\\
x_{Lj}
\end{pmatrix}.
$$

Thus,

$$
c_H(x_{Hj},x_{Lj})=\alpha_{HH}x_{Hj}+\alpha_{HL}x_{Lj},
\qquad
c_L(x_{Hj},x_{Lj})=\alpha_{LH}x_{Hj}+\alpha_{LL}x_{Lj}.
$$

For the baseline analysis, assume \(\alpha_{ts}\geq 0\). The asymmetric-peer
case has

$$
\alpha_{HL} \gg \alpha_{LH},
$$

often with \(\alpha_{LH}\) close to zero. The coefficient \(\alpha_{HL}\) is the
harm to an \(H\) tourist from an additional \(L\) tourist. The coefficient
\(\alpha_{LH}\) is the reverse effect. Own-type coefficients may be positive.

Each resort posts one price \(p_j\geq 0\). Marginal operating cost is normalized
to zero. A type-\(t\) tourist's utility from resort \(j\) is

$$
u_{tj}(x,p)=v_t-p_j-c_t(x_{Hj},x_{Lj}).
$$

The cartel maximizes total resort profit,

$$
\Pi(p,x)=\sum_{j=1}^J p_j(x_{Hj}+x_{Lj}).
$$

Because the resorts are identical, any asymmetric policy must be sustained by
the prices and resulting composition, not by an exogenous quality difference.

## 3. Tourist equilibrium given prices

Let \(x_{t0}\geq 0\) denote the mass of type \(t\) taking the outside option.
A feasible allocation satisfies

$$
x_{t0}+\sum_{j=1}^J x_{tj}=m_t
\qquad\text{for each }t.
$$

**Definition 1 (Wardrop-Nash equilibrium).** Given \(p=(p_1,\ldots,p_J)\), a
feasible allocation \(x\) is a Wardrop-Nash equilibrium if, for each type \(t\),
there is a number \(\bar u_t\geq 0\) such that

$$
x_{tj}>0 \ \Longrightarrow\ u_{tj}(x,p)=\bar u_t,
$$

$$
x_{tj}=0 \ \Longrightarrow\ u_{tj}(x,p)\leq \bar u_t,
$$

and

$$
x_{t0}>0 \ \Longrightarrow\ \bar u_t=0.
$$

Because tourists are nonatomic, a deviating tourist treats resort loads as
fixed. Under continuous costs, a Wardrop equilibrium exists. It need not be
unique because the asymmetric cross-congestion matrix need not generate a
potential game.

When all resorts in a tier charge the same price and have the same composition,
tourists of a given type are indifferent within that tier. If
\(\alpha_{HH},\alpha_{LL}>0\), equalization of own-type congestion gives a
symmetric allocation within each tier.

## 4. Symmetric pooling benchmark

Suppose every resort posts the same price \(p\), both types participate, and the
selected equilibrium is symmetric and pooled:

$$
x_{Hj}^{P}=\frac{m_H}{J},
\qquad
x_{Lj}^{P}=\frac{m_L}{J}
\qquad\text{for every }j.
$$

This allocation is always a Wardrop equilibrium when both types participate,
although other equilibria may coexist.

Define each type's net willingness to pay in the pooled allocation:

$$
w_H^P
=v_H-\frac{\alpha_{HH}m_H+\alpha_{HL}m_L}{J},
$$

$$
w_L^P
=v_L-\frac{\alpha_{LH}m_H+\alpha_{LL}m_L}{J}.
$$

Assume \(\min\{w_H^P,w_L^P\}\geq 0\). The largest common price that keeps both
types in the market is

$$
p^P=\min\{w_H^P,w_L^P\}.
$$

At equality, participation uses the tie-breaking convention that a tourist who
is indifferent to the outside option visits. Equivalently, all prices below can
be reduced by an arbitrarily small \(\varepsilon>0\).

The cartel's pooling profit is

$$
\boxed{\Pi^P=M p^P.}
$$

Total tourist rent in the pooling equilibrium is

$$
T^P
=m_H(w_H^P-p^P)+m_L(w_L^P-p^P).
$$

At least one type receives zero rent, but a common posted price generally leaves
positive rent to the other type.

For later use, total surplus under pooling is

$$
\begin{aligned}
W^P
={}&m_Hv_H+m_Lv_L\\
&-\frac{
\alpha_{HH}m_H^2
+(\alpha_{HL}+\alpha_{LH})m_Hm_L
+\alpha_{LL}m_L^2
}{J}.
\end{aligned}
$$

Since operating cost is zero,

$$
\Pi^P=W^P-T^P.
$$

This is a full-coverage pooling benchmark, not necessarily the globally optimal
symmetric policy. A symmetric cartel may instead exclude one type, or set a
price that induces partial participation. For example, a candidate
full-coverage \(H\)-only symmetric profit is

$$
\Pi_H^{\mathrm{only}}
=m_H\left(v_H-\frac{\alpha_{HH}m_H}{J}\right),
$$

provided that the implied price also deters \(L\) entry. An analogous expression
holds for a full-coverage \(L\)-only policy. A result that compares sorting with
every symmetric policy must also solve the feasible exclusion and
partial-participation branches.

## 5. Coordinated sorting

The cartel designates \(K\in\{1,\ldots,J-1\}\) resorts as premium resorts and
\(J-K\) resorts as budget resorts. All premium resorts post price \(p_H\), and
all budget resorts post price \(p_L\). The intended sorted allocation is

$$
x_{Hj}^S=\frac{m_H}{K},\quad x_{Lj}^S=0
\qquad\text{at each premium resort},
$$

and

$$
x_{Hj}^S=0,\quad x_{Lj}^S=\frac{m_L}{J-K}
\qquad\text{at each budget resort}.
$$

Define the four relevant congestion costs:

$$
h_K=\frac{\alpha_{HH}m_H}{K},
\qquad
\ell_K=\frac{\alpha_{LL}m_L}{J-K},
$$

$$
z_{HL,K}=\frac{\alpha_{HL}m_L}{J-K},
\qquad
z_{LH,K}=\frac{\alpha_{LH}m_H}{K}.
$$

Here \(h_K\) and \(\ell_K\) are on-path own-type congestion costs.
\(z_{HL,K}\) is the cost an \(H\) tourist would experience by deviating to a
budget resort, and \(z_{LH,K}\) is the cost an \(L\) tourist would experience by
deviating to a premium resort.

### 5.1 Incentive compatibility and participation

The intended allocation is a Wardrop equilibrium if and only if the following
constraints hold:

$$
\tag{IC-H}
p_H+h_K\leq p_L+z_{HL,K},
$$

$$
\tag{IC-L}
p_L+\ell_K\leq p_H+z_{LH,K},
$$

$$
\tag{IR-H}
p_H+h_K\leq v_H,
$$

$$
\tag{IR-L}
p_L+\ell_K\leq v_L.
$$

The first two conditions make sorting self-enforcing. No resort observes type.
High types voluntarily pay for the premium tier because the budget tier contains
low types. Low types remain in the budget tier because the premium price is high
enough to offset its peer environment.

It is useful to define generalized prices paid by each intended type:

$$
q_H=p_H+h_K,
\qquad
q_L=p_L+\ell_K.
$$

Also define

$$
A_K=z_{HL,K}-\ell_K
=\frac{(\alpha_{HL}-\alpha_{LL})m_L}{J-K},
$$

$$
B_K=h_K-z_{LH,K}
=\frac{(\alpha_{HH}-\alpha_{LH})m_H}{K}.
$$

The two IC constraints become

$$
\boxed{B_K\leq q_H-q_L\leq A_K.}
$$

Thus, \(A_K\) is the largest generalized premium that high types will accept
relative to the budget tier. A larger \(\alpha_{HL}\) raises \(A_K\), relaxes
\((IC\text{-}H)\), and allows the cartel to extract more surplus from high types.
The lower bound \(B_K\) captures low-type invasion. If low types find the
premium peer environment attractive, the premium price must be sufficiently
high to keep them out.

Price-based sorting is IC-feasible for a given \(K\) only if

$$
\boxed{A_K\geq B_K.}
$$

Equivalently,

$$
z_{HL,K}+z_{LH,K}\geq h_K+\ell_K.
$$

This condition is often omitted in informal accounts of elite sorting. Strong
one-way aversion helps deter high types from entering the budget tier, but weak
low-type aversion can make the premium tier attractive to low types. Both IC
constraints matter.

The term "premium" describes the intended composition. It does not by itself
guarantee \(p_H>p_L\). Since

$$
p_H-p_L=(q_H-q_L)-h_K+\ell_K,
$$

a model that requires the premium resort to post a strictly higher observable
price must add \(q_H-q_L>h_K-\ell_K\).

### 5.2 Optimal screening prices for a fixed resort split

Let

$$
d=v_H-v_L\geq 0.
$$

First solve the screening problem without the nonnegative-price lower bounds.
For a given \(K\), call the split **admissible** if \(A_K\geq B_K\) and the
solution derived below satisfies

$$
q_H^*\geq h_K,\qquad q_L^*\geq \ell_K,
$$

so that \(p_H^*,p_L^*\geq 0\). For a nonadmissible split with \(A_K\geq B_K\),
the constrained problem can instead be solved by adding these two lower bounds.
The nonnegativity requirement can be dropped if subsidies are allowed.

**Proposition 1 (optimal full-coverage separating prices for fixed \(K\)).** For
an admissible \(K\), the cartel-optimal generalized prices among prices that
serve all of both types are:

$$
(q_H^*,q_L^*)=
\begin{cases}
(v_L+A_K,\ v_L), & d>A_K,\\[3pt]
(v_H,\ v_L), & B_K\leq d\leq A_K,\\[3pt]
(v_H,\ v_H-B_K), & d<B_K.
\end{cases}
$$

The corresponding posted prices are

$$
p_H^*=q_H^*-h_K,
\qquad
p_L^*=q_L^*-\ell_K.
$$

Total tourist rent under optimal sorting is

$$
\boxed{
R_K
=m_H(d-A_K)_+
+m_L(B_K-d)_+,
}
$$

where \((z)_+=\max\{z,0\}\).

**Proof.** For fixed \(K\), congestion costs and quantities are fixed. The
cartel maximizes

$$
m_H(q_H-h_K)+m_L(q_L-\ell_K)
$$

subject to

$$
q_H\leq v_H,\qquad q_L\leq v_L,\qquad
B_K\leq q_H-q_L\leq A_K.
$$

The objective is strictly increasing in both generalized prices. If
\(d>A_K\), both IR constraints cannot bind because their implied difference is
\(d>A_K\). Then \(q_L=v_L\) and \((IC\text{-}H)\) binds, so
\(q_H=v_L+A_K\). If \(B_K\leq d\leq A_K\), both IR constraints bind. If
\(d<B_K\), both IR constraints cannot bind because their implied difference is
below \(B_K\). Then \(q_H=v_H\) and \((IC\text{-}L)\) binds, so
\(q_L=v_H-B_K\). Tourist rents equal \(m_t(v_t-q_t^*)\), which gives the stated
formula. \(\square\)

The middle case is full surplus extraction. In that case,

$$
B_K\leq v_H-v_L\leq A_K,
$$

and the differentiated resort policies implement the same allocation and
payments that direct type-contingent pricing would implement. This is
second-degree price discrimination: resort choice reveals type.

The high type's information rent is

$$
m_H(d-A_K)_+.
$$

An increase in \(\alpha_{HL}\) raises \(A_K\) and reduces this rent one for one
until it reaches zero. This is the precise sense in which asymmetric peer
congestion is a screening instrument.

### 5.3 Sorted profit

Total surplus under the sorted allocation is

$$
W^S(K)
=m_Hv_H+m_Lv_L
-\frac{\alpha_{HH}m_H^2}{K}
-\frac{\alpha_{LL}m_L^2}{J-K}.
$$

Cross-type congestion disappears, but each type is concentrated in fewer
resorts. Proposition 1 implies

$$
\boxed{
\Pi^S(K)=W^S(K)-R_K.
}
$$

## 6. When does coordinated sorting increase cartel profit?

The real-surplus effect of sorting is

$$
\begin{aligned}
\Delta W(K)
={}&W^S(K)-W^P\\
={}&
\underbrace{
\frac{(\alpha_{HL}+\alpha_{LH})m_Hm_L}{J}
}_{\text{cross-type congestion relief}}\\
&-
\underbrace{
\alpha_{HH}m_H^2\left(\frac{1}{K}-\frac{1}{J}\right)
+\alpha_{LL}m_L^2\left(\frac{1}{J-K}-\frac{1}{J}\right)
}_{\text{own-type concentration cost}}.
\end{aligned}
$$

The profit effect also includes the change in tourist rents.

**Proposition 2 (exact sorting-dominance condition).** For any admissible
\(K\), coordinated sorting strictly increases total cartel profit relative to
the symmetric pooling benchmark if and only if

$$
\boxed{
\Delta W(K)+T^P-R_K>0.
}
$$

Equivalently,

$$
\boxed{
\begin{aligned}
&
\frac{(\alpha_{HL}+\alpha_{LH})m_Hm_L}{J}
-\alpha_{HH}m_H^2\left(\frac{1}{K}-\frac{1}{J}\right)\\
&\quad
-\alpha_{LL}m_L^2\left(\frac{1}{J-K}-\frac{1}{J}\right)
+T^P
-m_H(d-A_K)_+
-m_L(B_K-d)_+
>0.
\end{aligned}
}
$$

Therefore, some coordinated full-coverage sorted policy in the characterized
class dominates full-coverage pooling if and only if the maximum of the
left-hand side over admissible
\(K\in\{1,\ldots,J-1\}\) is positive.

**Proof.** Pooling profit is \(\Pi^P=W^P-T^P\). Sorted profit is
\(\Pi^S(K)=W^S(K)-R_K\). Subtracting gives

$$
\Pi^S(K)-\Pi^P=\Delta W(K)+T^P-R_K.
$$

Substituting the expressions for \(\Delta W(K)\) and \(R_K\) yields the second
condition. \(\square\)

Proposition 2 separates three forces:

1. Sorting removes cross-type peer costs.
2. Sorting increases own-type congestion by assigning each type fewer resorts.
3. Sorting replaces the rent left by a common pooling price, \(T^P\), with the
   screening rents required under separation, \(R_K\).

The result is not simply that a large \(\alpha_{HL}\) makes sorting profitable.
A large \(\alpha_{HL}\) raises real surplus and relaxes high-type IC, but sorting
can still fail because own-type concentration is severe, low types invade the
premium tier, or the required posted prices are negative.

### 6.1 Optimal number of premium resorts

Suppose the optimal split lies in the full-extraction region,

$$
B_K\leq d\leq A_K,
$$

so \(R_K=0\). Since \(T^P\) and cross-type congestion relief do not depend on
\(K\), the cartel chooses \(K\) to minimize

$$
C^S(K)
=\frac{\alpha_{HH}m_H^2}{K}
+\frac{\alpha_{LL}m_L^2}{J-K}.
$$

Treating \(K\) as continuous and assuming
\(\alpha_{HH},\alpha_{LL}>0\), the unique interior minimizer is

$$
\boxed{
\frac{K^*}{J}
=
\frac{\sqrt{\alpha_{HH}}\,m_H}
{\sqrt{\alpha_{HH}}\,m_H+\sqrt{\alpha_{LL}}\,m_L}.
}
$$

Thus, the premium tier receives more resorts when high types are more numerous
or have a larger own-type congestion coefficient. With integer \(K\), choose
the best admissible neighboring integer. If the continuous \(K^*\) violates IC
or nonnegative-price constraints, the cartel solves the one-dimensional finite
problem in Proposition 2.

At the continuous optimum,

$$
C^S(K^*)
=\frac{
\left(\sqrt{\alpha_{HH}}\,m_H+\sqrt{\alpha_{LL}}\,m_L\right)^2
}{J}.
$$

This gives a particularly transparent result.

**Corollary 1 (clean interior condition).** Suppose \(K^*\) is admissible and
satisfies

$$
B_{K^*}\leq d\leq A_{K^*}.
$$

Then

$$
\boxed{
\Pi^S(K^*)-\Pi^P
=
\frac{
\left(\alpha_{HL}+\alpha_{LH}
-2\sqrt{\alpha_{HH}\alpha_{LL}}\right)m_Hm_L
}{J}
+T^P.
}
$$

Hence coordinated sorting strictly dominates pooling if and only if

$$
\boxed{
\frac{
\left(\alpha_{HL}+\alpha_{LH}
-2\sqrt{\alpha_{HH}\alpha_{LL}}\right)m_Hm_L
}{J}
+T^P>0.
}
$$

If one compares total surplus rather than profit, the condition is simply

$$
\alpha_{HL}+\alpha_{LH}
>2\sqrt{\alpha_{HH}\alpha_{LL}}.
$$

Under nearly one-way peer aversion, \(\alpha_{LH}\simeq 0\), a sufficiently
large \(\alpha_{HL}\) alone can satisfy this condition. The additional
\(T^P\) term shows that the cartel may profit from sorting even when sorting
slightly lowers total surplus, because sorting improves price discrimination.

To show that sorting dominates every symmetric policy, rather than only the
pooling benchmark, one must additionally compare it with the optimal feasible
symmetric exclusion and partial-participation branches. For the two
full-coverage exclusion candidates above, the additional comparisons are

$$
\Pi^S(K)>\Pi_H^{\mathrm{only}}
\qquad\text{and}\qquad
\Pi^S(K)>\Pi_L^{\mathrm{only}}
$$

when those branches are feasible.

### 6.2 Canonical one-way-aversion case

The mechanism is especially transparent under the following stark asymmetry:

$$
\alpha_{HH}=0,\qquad
\alpha_{LH}=0,\qquad
\alpha_{LL}>0,\qquad
\alpha_{HL}>\alpha_{LL}.
$$

High types care only about the presence of low types. Low types do not mind high
types, although they dislike congestion from other low types. Then \(B_K=0\)
and

$$
A_K=\frac{(\alpha_{HL}-\alpha_{LL})m_L}{J-K}>0.
$$

If

$$
d\leq \frac{(\alpha_{HL}-\alpha_{LL})m_L}{J-1}
\qquad\text{and}\qquad
v_L\geq \frac{\alpha_{LL}m_L}{J-1},
$$

one premium resort and \(J-1\) budget resorts implement full extraction at

$$
p_H=v_H,
\qquad
p_L=v_L-\frac{\alpha_{LL}m_L}{J-1}.
$$

Among full-extraction splits, \(K=1\) is optimal because high-type
concentration is costless and giving more resorts to low types reduces their
own-type congestion. Proposition 2 becomes

$$
\boxed{
\Pi^S(1)-\Pi^P
=
\frac{\alpha_{HL}m_Hm_L}{J}
-\frac{\alpha_{LL}m_L^2}{J(J-1)}
+T^P.
}
$$

Thus, in this canonical one-way case, coordinated sorting dominates pooling if
and only if

$$
\alpha_{HL}m_H
>
\frac{\alpha_{LL}m_L}{J-1}-\frac{JT^P}{m_L}.
$$

The high type's one-way dislike is the source of both the removed externality
and the IC wedge that permits the premium price.

## 7. Interpretation of asymmetric peer congestion

The asymmetry has two distinct roles.

First, \(\alpha_{HL}\) contributes to the real-surplus gain from eliminating
cross-type contact. If high types suffer from low-type presence and low types
are approximately indifferent to high-type presence, sorting removes a real
loss for high types without removing a corresponding benefit for low types.

Second, \(\alpha_{HL}\) relaxes high-type IC:

$$
q_H-q_L\leq
\frac{(\alpha_{HL}-\alpha_{LL})m_L}{J-K}.
$$

The budget tier becomes an unattractive outside option for high types. The
cartel can therefore charge a higher effective premium and extract high-type
surplus.

There is also an opposing low-type IC force:

$$
q_H-q_L\geq
\frac{(\alpha_{HH}-\alpha_{LH})m_H}{K}.
$$

If low types do not mind high types, the premium tier may be attractive to them.
Price alone deters this invasion only when the premium is sufficiently
expensive. Thus, one-way aversion is helpful through \(\alpha_{HL}\), but a low
\(\alpha_{LH}\) does not mechanically help every constraint. A rigorous account
must check \(A_K\geq B_K\).

## 8. What changes or breaks the result?

### 8.1 Symmetric peer effects

If \(\alpha_{HL}=\alpha_{LH}>0\), cross-type contact is mutually costly.
Sorting can then generate a larger real-surplus gain and can make both types
prefer separation. The mechanism is no longer specifically elite avoidance of
low types. It is mutual segregation.

At the opposite extreme, suppose every tourist experiences every peer in the
same way:

$$
\alpha_{HH}=\alpha_{HL}=\alpha_{LH}=\alpha_{LL}=\alpha.
$$

Then \(A_K=B_K=0\), and resort labels provide no screening content. In the
continuous relaxation, the equal-load split gives an optimized real-surplus
gain of zero. With integer constraints, the optimized real-surplus gain is
weakly negative. Any apparent gain from sorting disappears after accounting for
the information rent required to induce high types to pay more.

### 8.2 Aspirational low types

Suppose low types enjoy proximity to high types, so

$$
\alpha_{LH}<0.
$$

Then pooling creates an aspirational benefit for low types. Sorting destroys
that benefit, reducing the cross-type relief term
\((\alpha_{HL}+\alpha_{LH})m_Hm_L/J\). It also raises

$$
B_K=\frac{(\alpha_{HH}-\alpha_{LH})m_H}{K},
$$

which makes low-type invasion of premium resorts harder to deter. Aspirational
preferences therefore weaken sorting through both the surplus channel and the
IC channel. If \(\alpha_{LH}\) is sufficiently negative, price-only separation
may be infeasible or unprofitable even when high types strongly dislike low
types.

### 8.3 Large own-type congestion

Sorting concentrates each type in fewer resorts. When
\(\alpha_{HH}\) or \(\alpha_{LL}\) is large, the concentration cost can exceed
the removed cross-type cost. This is the central technological tradeoff in
Proposition 2.

### 8.4 Failure of price-only screening

If \(A_K<B_K\) for every \(K\), no pair of posted prices supports complete
separation. A high premium price is needed to deter low types, but that same
price sends high types to the budget tier. Partial mixing, exclusion, or an
additional policy instrument is then necessary.

### 8.5 Cartel enforceability and transfers

The analysis maximizes total profit and permits transfers among resorts.
Without transfers, premium and budget resorts may disagree about the policy
because their individual profits differ. Without cartel enforcement, a resort
may profitably deviate by changing its price and attracting both types. Those
questions require a noncooperative pricing game among resorts and are distinct
from the present joint-profit comparison.

### 8.6 Partial participation and exclusion

With an outside option and homogeneous tourists within each type, a price can
induce only part of a type to enter, with entrants receiving zero utility.
The cartel may use this channel to reduce congestion or restrict quantity.
Propositions 1 and 2 remain exact for the full-coverage branches, but they do
not by themselves establish the unrestricted global cartel optimum.

The unrestricted problem can be written by allowing served masses
\(\widehat m_H\in[0,m_H]\) and \(\widehat m_L\in[0,m_L]\), replacing \(m_t\)
by \(\widehat m_t\) throughout the equilibrium and IC constraints, and
maximizing over both served masses and \(K\). Boundary solutions include
type exclusion. This extension preserves the screening logic but makes the
quantity choice part of the concentration tradeoff.

## 9. Wrong equilibrium traps and evolutionary dynamics

The symmetric pooled allocation is a Wardrop equilibrium whenever all resorts
post the same price and both types participate. This remains true even when a
sorted policy would yield higher cartel profit and higher total surplus. Since
resorts are intrinsically identical, tourists need coordinated policy
differences or coordinated expectations to move from pooling to sorting.

This creates a wrong equilibrium trap. Starting from pooling, one resort may be
unable to become premium by raising its price alone because it initially has no
better peer composition. Conversely, a nominally premium resort may be invaded
by low types unless its price and expected high-type presence jointly satisfy
the IC constraints.

A standard within-type replicator dynamic is

$$
\dot y_{tj}
=y_{tj}\left(u_{tj}-\bar u_t\right),
$$

where \(y_{tj}=x_{tj}/m_t\) is type \(t\)'s share choosing resort \(j\), with an
outside-option strategy added when participation is endogenous. Wardrop
equilibria are rest points of this dynamic.

For intuition, consider two equal-price resorts and perturb the symmetric
allocation by moving masses \((\delta_H,\delta_L)\) from resort 2 to resort 1.
The first-order payoff difference between resorts for type \(t\) is

$$
u_{t1}-u_{t2}
=-2(\alpha_{tH}\delta_H+\alpha_{tL}\delta_L).
$$

The linearized adjustment matrix is proportional to

$$
-\operatorname{diag}(m_H,m_L)
\begin{pmatrix}
\alpha_{HH} & \alpha_{HL}\\
\alpha_{LH} & \alpha_{LL}
\end{pmatrix}.
$$

With positive own-type coefficients, the pooled state is locally stable under
this two-resort adjustment when

$$
\alpha_{HH}\alpha_{LL}>\alpha_{HL}\alpha_{LH}.
$$

It is unstable when the reverse inequality holds. In the strongly one-way case
\(\alpha_{LH}\simeq 0\), pooling can remain locally stable even when
\(\alpha_{HL}\) is very large and coordinated sorting is more profitable. This
is a particularly clear wrong-equilibrium trap: unilateral tourist adjustment
does not create the sorted outcome.

Under differentiated policies, a sorted state with strict cross-tier IC is
locally resistant to cross-tier invasion. Positive own-type congestion
equalizes tourists within each tier. If an IC constraint binds, the state is
only weakly resistant and small shocks or mutations can create mixing. Because
replicator dynamics leave zero-share strategies at zero, equilibrium selection
also depends on initial conditions, experimentation, and whether resorts can
coordinate a simultaneous policy change.

## 10. Extensions

### Capacity

A capacity cap changes equilibrium congestion and can reduce the concentration
cost of uncontrolled entry, but a generic cap does not by itself distinguish
types. It supports screening only when paired with a rule that selects high
willingness-to-pay tourists, such as an auction, minimum spend, priority
booking, or a sufficiently high price.

### Branding and amenities

Let resort \(j\) choose a brand or amenity \(b_j\) that changes gross values to
\(v_t(b_j)\). A premium brand supports sorting when it raises
\(v_H(b_j)-v_L(b_j)\), or otherwise makes the premium option relatively more
attractive to high types. In the present notation, branding shifts the value
gap \(d\) and therefore changes whether \(B_K\leq d\leq A_K\).

### Hard budgets

If low types face a hard budget \(\bar p_L\), then choosing
\(p_H>\bar p_L\) directly prevents low-type invasion. This removes or relaxes
\((IC\text{-}L)\), making price-only sorting easier. The current model is more
demanding because sorting must work through preferences rather than an
exogenous inability to pay.

### More than two types

With a continuum of types, resorts form a menu of peer environments and prices.
The two-type bounds \(B_K\leq q_H-q_L\leq A_K\) become adjacent-type IC
constraints. A single-crossing condition on type-specific peer costs is the
natural requirement for monotone sorting.

## 11. Main conclusion

Coordinated differentiation among identical resorts can strictly increase total
cartel profit relative to full-coverage pooling. The exact condition within the
full-coverage class is Proposition 2:

$$
\text{cross-type congestion relief}
-\text{own-type concentration cost}
+\text{pooling rent recovered}
-\text{sorting rent required}
>0.
$$

Asymmetric peer congestion is central because a large
\(\alpha_{HL}\) both removes a costly externality and makes the low-price,
low-type resort unattractive to high types. This supports second-degree price
discrimination. However, asymmetry alone is not sufficient. Low-type invasion,
own-type congestion, participation, equilibrium selection, and symmetric
exclusion alternatives must all be checked.
