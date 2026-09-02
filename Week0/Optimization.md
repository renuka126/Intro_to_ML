# Optimization — Week 4 Tutorial 4
*NPTEL: Introduction to Machine Learning (Balaraman Ravindran)*

## Mathematical Optimization
- **Definition:** Mathematical optimization is picking the *best* element (based on some criteria) from a set of available alternatives
- General form:
  - **minimize** f₀(x)
  - **subject to** fᵢ(x) ≤ bᵢ, for i = 1, 2, …, m
- Terms:
  - x ∈ ℝⁿ is the **optimization variable**
  - f₀ : ℝⁿ → ℝ is the **objective function** (what we're trying to minimize)
  - fᵢ : ℝⁿ → ℝ are the **constraints**

## Optimal Solution
- A vector x ∈ ℝⁿ is a solution to the problem if:
  - It satisfies **all** the constraints
  - f₀(x) is the **minimum possible value** in that feasible region
- Such a point is called **x\*** — the **optimal solution**

## Examples
**Data fitting:**
- Variables: parameters of the model
- Constraints: parameter limits, prior information
- Objective: measure of fit (e.g., minimizing error)

**Portfolio Optimization:**
- Variables: amounts invested in different assets
- Constraints: budget, max/min investment per asset, minimum return
- Objective: overall risk or return variance

## Solving Optimization Problems
- Optimization problems are generally **hard** to solve
- They're classified into classes based on properties of the objective and constraints
- Some classes are efficiently solvable:
  - Linear programs
  - Least Squares problems
  - Convex Optimization problems
- **Convex optimization** is emphasized since it comes up very frequently in ML

## Convex Set
- A set **C** is convex if, for any two points a, b ∈ C, the entire line segment joining them also lies in C:
  c = θa + (1−θ)b, c ∈ C, for all θ ∈ [0,1]
- *(Simply: if you pick any 2 points inside the shape and draw a straight line between them, that line never leaves the shape.)*
- **Convex combination:** a point of the form θ₁x₁ + θ₂x₂ + … + θₖxₖ, where Σθᵢ = 1 and θᵢ ≥ 0

## Convex Function
- f : ℝⁿ → ℝ is **convex** if:
  - Its domain is a convex set
  - For all x, y in the domain, and 0 ≤ θ ≤ 1:
    **f(θx + (1−θ)y) ≤ θf(x) + (1−θ)f(y)**
- *(Simply: the curve of the function always lies below (or on) the straight line connecting any two points on it — like a bowl shape.)*

### Strictly Convex Functions
- Same condition but with strict inequality: f(θx + (1−θ)y) < θf(x) + (1−θ)f(y), when x ≠ y

### Concave & Strictly Concave
- f is **concave** if −f is convex
- f is **strictly concave** if −f is strictly convex

**Example:** f(x) = x² is a classic convex function (a simple upward-opening parabola)

## Conditions for Convexity

### First Order Condition
- If f is differentiable (∇f exists everywhere in its domain), f is convex if and only if:
  - dom(f) is convex
  - **f(y) ≥ f(x) + ∇f(x)ᵀ(y − x)**, for all x, y in dom(f)
- *(Simply: the function always lies above its tangent line/plane at any point.)*

### Second Order Condition
- If f is twice differentiable (Hessian ∇²f exists), f is convex if and only if:
  - dom(f) is convex
  - Its Hessian is **positive semi-definite**: ∇²f(x) ⪰ 0, for all x in dom(f)
- In plain 1-D calculus terms, this just reduces to **f″(x) ≥ 0**
- The Hessian matrix H contains all the second partial derivatives:
  H = [[∂²f/∂x₁², ∂²f/∂x₁∂x₂, …], [∂²f/∂x₂∂x₁, ∂²f/∂x₂², …], …]

## Epigraph
- The **epigraph** of f: epi f = {(x,t) | x ∈ dom(f), t ≥ f(x)} — basically the region *above* the function's graph
- **Key fact:** f is a convex function ⇔ epi f is a convex set

## Sublevel Sets
- The **α-sublevel set** of f: C(α) = {x ∈ dom(f) | f(x) ≤ α}
- If f is convex ⟹ its sublevel sets are convex
- **Note:** the converse is *not* true (having convex sublevel sets doesn't guarantee f itself is convex)

## Properties (Convexity-Preserving Operations)
- **Non-negative weighted sum:** Σαᵢfᵢ is convex if all αᵢ ≥ 0 and each fᵢ is convex
- **Composition with affine function:** f(Ax + b) is convex if f is convex
- **Pointwise maximum/supremum:** if f₁, f₂ are convex, then max{f₁(x), f₂(x)} is convex
- **Minimization:** if f(x,y) is convex in (x,y) and C is a convex set, then g(x) = inf_(y∈C) f(x,y) is convex
- **Important consequence:** for convex functions, **any local minimum is also the global minimum**

## Jensen's Inequality
- For a convex function f, points x₁, x₂, …, xₙ, and weights θᵢ ≥ 0 with Σθᵢ = 1:
  **f(θ₁x₁ + θ₂x₂ + … + θₙxₙ) ≤ Σθᵢf(xᵢ)**
- In words: **the value of the average is less than (or equal to) the average of the values**

## Optimization Problem (General Form)
- min f₀(x)
- s.t. fᵢ(x) ≤ 0, i = 1,…,m
- s.t. hᵢ(x) = 0, i = 1,…,p
- The optimal value p\* is defined as:
  p\* = inf{f₀(x) | fᵢ(x) ≤ 0 for all i, and hᵢ(x) = 0 for all i}
- We use **infimum** rather than **min** because the minimum might not actually be *achieved* by any point in the feasible set (it could just be approached in the limit) — infimum always exists even then

## Duality
- Every optimization problem has two perspectives: the **primal form** and the **dual form**
- Solving/understanding the dual helps us understand the behavior of the primal
- Standard primal form:
  - min f₀(x)
  - s.t. fᵢ(x) ≤ 0, i = 1,…,m
  - s.t. aᵢᵀx = bᵢ, i = 1,…,p
- Let 𝔻 be the domain. This is the **primal problem**, with optimal value **p\*** attained at **x\***

## Lagrangian
- Consider a "relaxed" version of the problem that folds the constraints into the objective using multipliers λᵢ ≥ 0 and νᵢ:
  min f₀(x) + Σλᵢfᵢ(x) + Σνᵢhᵢ(x)
- This combined expression is the **Lagrangian**:
  **L(x, λ, ν) = f₀(x) + Σλᵢfᵢ(x) + Σνᵢhᵢ(x)**
- Key inequality: inf_x L(x, λ, ν) ≤ L(x\*, λ, ν) ≤ p\*
- Define: **g(λ, ν) = inf_x L(x, λ, ν)**

## Lagrangian Dual Problem
- Since g(λ, ν) ≤ p\*, **g forms a lower bound on the optimal value of the primal problem**
- **Dual problem:**
  - max g(λ, ν)
  - s.t. λᵢ ≥ 0, i = 1,…,m
- The optimal value of the dual is attained at λ\*, ν\*
- The dual is **always concave**, regardless of the shape of the primal — so it's always solvable in principle
- Optimal dual value is denoted **d\***
- **p\* − d\*** is known as the **duality gap**

## Strong and Weak Duality
- If the duality gap is 0 (p\* = d\*), this is called **Strong Duality**
- Primal can also be written as: p\* = inf_x sup_(λ≥0,ν) L(x, λ, ν)
- Dual can be written as: d\* = sup_(λ≥0,ν) inf_x L(x, λ, ν)
- If strong duality holds, the order of inf and sup **doesn't matter** — the optimal variables sit at a **saddle point** of the Lagrangian

## Slater's Condition
- A **sufficiency condition** for strong duality to hold
- In a convex optimization problem: if there exists a point x in the *interior* (relint 𝔻) such that fᵢ(x) < 0 (strictly) and hᵢ(x) = 0, then **strong duality holds**
- *(Simply: as long as there's some strictly feasible point inside the feasible region — not just on its boundary — strong duality is guaranteed.)*
