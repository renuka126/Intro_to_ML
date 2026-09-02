# Linear Algebra — Week 2 Tutorial 2 (Part 1)
*NPTEL: Introduction to Machine Learning (Balaraman Ravindran) — Tutorial by Abhinav Garlapati, Varun Gangal*

## What is Linear Algebra
- Linear algebra is the branch of math dealing with **vector spaces** and **linear mappings** between them
- Covers lines, planes, subspaces, and properties common to all vector spaces
- **Why we study it:**
  - Gives a compact way to represent and solve systems of linear equations
  - In ML, data is represented as matrices — so linear algebra tools are naturally used

## Introduction to Linear Algebra
- Example system of equations:
  - 4x₁ − 5x₂ = −13
  - −2x₁ + 3x₂ = 9
- Written compactly in matrix form as **Ax = b**, where:
  - A = [[4, −5], [−2, 3]]
  - b = [−13, 9]

## Vector Space
- A set **V** with two operations (+ and ·) is a **vector space** if it's closed under both operations and satisfies 8 rules (axioms):

1. **Commutative Law:** x + y = y + x
2. **Associative Law:** (x + y) + z = x + (y + z)
3. **Additive identity:** there's a 0 in V such that x + 0 = x
4. **Additive inverse:** for every x, there's an x̃ such that x + x̃ = 0
5. **Distributive Law:** α·(x + y) = α·x + α·y
6. **Distributive Law:** (α + β)·x = α·x + β·x
7. **Associative Law:** (αβ)·x = α·(β·x)
8. **Unitary Law:** 1·x = x

*(In simple terms: a vector space is just a collection of things — vectors — that you can add together and scale by numbers, and it still behaves the way you'd expect.)*

## Subspace
- If **W** is a subset of a vector space **V**, and W is itself a vector space, then W is a **subspace** of V
- You don't need to check all 8 axioms every time — there's a shortcut:
  - **Theorem:** W is a subspace of V if and only if W is non-empty and
    x + αy ∈ W, for all x, y ∈ W and α ∈ ℝ

## Norm
- A **norm** is any function f : ℝⁿ → ℝ that measures the "size" or "length" of a vector, satisfying:
  1. f(x) ≥ 0 for all x (**non-negativity**)
  2. f(x) = 0 only if x = 0 (**definiteness**)
  3. f(tx) = |t|·f(x) (**homogeneity** — scaling the vector scales its length the same way)
  4. f(x + y) ≤ f(x) + f(y) (**triangle inequality**)
- **Example — lₚ norm:** ‖x‖ₚ = (Σ|xᵢ|ᵖ)^(1/p)
- **Matrices have norms too — e.g., Frobenius norm:**
  ‖A‖_F = √(ΣᵢΣⱼ Aᵢⱼ²) = √(tr(AᵀA))

## Range of a Matrix
- The **span** of vectors {x₁, x₂, …, xₙ} is the set of all vectors you can build by combining them (scaled and added together)
- The **range (or columnspace)** of matrix A, written R(A), is the span of its columns — all the linear combinations of A's columns
- **Example:** For A = [[1,0],[5,4],[2,4]], the columnspace is the plane spanned by [1,5,2]ᵀ and [0,4,4]ᵀ

## Nullspace of a Matrix
- The **nullspace** N(A) of a matrix A (size m×n) is the set of all vectors x that become 0 when multiplied by A:
  N(A) = {x ∈ ℝⁿ : Ax = 0}
- The size (dimension) of the nullspace is called the **nullity** of A
- Note: vectors in N(A) have dimension n, while vectors in R(A) have dimension m — so vectors in R(Aᵀ) and N(A) are both dimension n

**Example:** For A = [[1,0],[5,4],[2,4]], solving Ax = 0 shows the nullspace contains only the zero vector (0,0) — nothing else maps to zero.

## Linear Independence and Rank
- A set of vectors {x₁, x₂, …, xₙ} is **linearly independent** if none of them can be written as a combination of the others
  - If xₙ = Σαᵢxᵢ for some scalars, the vectors are **linearly dependent**; otherwise they're **independent**
- **Column rank** of matrix A = size of the largest set of linearly independent columns
- **Row rank** = largest set of linearly independent rows

## Properties of Ranks
- For any matrix A (m×n), the **column rank always equals the row rank** — this common value is just called the **rank(A)**
- Basic properties:
  1. rank(A) ≤ min(m, n). If rank(A) = min(m, n), A is called **full rank**
  2. rank(A) = rank(Aᵀ)
  3. For A (m×n), B (n×p): rank(AB) ≤ min(rank(A), rank(B))
  4. For A, B (m×n): rank(A + B) ≤ rank(A) + rank(B)

## Orthogonal Matrices
- A square matrix U is **orthogonal** if:
  - All columns are mutually perpendicular (orthogonal): vᵢᵀvⱼ = 0 for i ≠ j
  - All columns have length 1 (normalized): vᵢᵀvᵢ = 1
- If U is orthogonal: **UUᵀ = UᵀU = I** — meaning U's inverse is just its transpose
- Multiplying a vector by an orthogonal matrix **doesn't change its length**: ‖Ux‖₂ = ‖x‖₂
  - Think of it as a pure **rotation** — direction changes, but magnitude stays the same

## Quadratic Forms & Definiteness
- For a square matrix A (n×n) and vector x ∈ ℝⁿ, the scalar **xᵀAx** is called a **quadratic form**
- A symmetric matrix A is:
  - **Positive definite (PD)** if xᵀAx > 0 for all non-zero x
  - **Positive semidefinite** if xᵀAx ≥ 0
  - **Negative definite** if xᵀAx < 0
  - **Negative semidefinite** if xᵀAx ≤ 0
- Positive/negative definite matrices are always **full rank**, and therefore **invertible**
- **Gram matrix:** for any matrix A (m×n), G = AᵀA is always **positive semidefinite**
  - If m ≥ n, then G is **positive definite**
