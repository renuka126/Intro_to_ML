# Linear Algebra — Week 2 Tutorial 2 (Part 2)
*NPTEL: Introduction to Machine Learning (Balaraman Ravindran) — Tutorial by Abhinav Garlapati, Varun Gangal*

## Eigenvalues & Eigenvectors
- For a square matrix **A** (n×n), λ is an **eigenvalue** of A and vector x⃗ is its **eigenvector** if:
  **Ax⃗ = λx⃗**
- **Geometric meaning:** an eigenvector is a vector that, when multiplied by A, only gets **scaled** (stretched/shrunk) — it doesn't change direction (isn't rotated)

**Example:**
- A = [[6,5],[1,2]], x⃗ = [5,1]
- Ax⃗ = [35,7] = 7·x⃗ → so λ = 7 is an eigenvalue here

## Characteristic Equation
- Trivially, the zero vector would always satisfy Ax⃗ = λx⃗, so we only count **non-zero** vectors as eigenvectors
- To find all eigenvalue-eigenvector pairs of A:
  - Ax⃗ = λx⃗ → Ax⃗ − λIx⃗ = 0 → (A − λI)x⃗ = 0
  - This only holds (for non-zero x⃗) if **|A − λI| = 0**
- This equation is called the **characteristic equation** of A
- Solving it gives all the eigenvalues λ of A — note these can be **complex numbers**

## Properties of Eigenvalues
1. The **trace** tr(A) (sum of diagonal elements) equals the sum of all eigenvalues:
   tr(A) = Σλᵢ
2. The **determinant** |A| equals the product of all eigenvalues:
   |A| = Πλᵢ
3. The **rank** of A equals the number of **non-zero** eigenvalues
4. If A is invertible, the eigenvalues of A⁻¹ are 1/λᵢ (just the reciprocals)

## Proof — Eigenvectors with Distinct Eigenvalues are Independent
- (Sketch) Assume a smallest linearly dependent set of eigenvectors exists with distinct eigenvalues
- Applying (A − λₖI) to the dependency relation and simplifying leads to a smaller dependent set — contradicting the "smallest" assumption
- **Conclusion:** eigenvectors corresponding to distinct eigenvalues are linearly independent

## Diagonalization
- Given matrix A, build matrix **S** where each column is an eigenvector of A: S = [v⃗₁, v⃗₂, …, v⃗ₙ]
- Then: AS = [λ₁v⃗₁, λ₂v⃗₂, …, λₙv⃗ₙ] = S·Λ, where Λ is a diagonal matrix of eigenvalues
- So: **AS = SΛ → A = SΛS⁻¹**
- This means S⁻¹AS is diagonal
- **Important:** this only works if S is invertible — true when all eigenvalues are distinct (so eigenvectors are independent)

## Properties of Diagonalization
- A square matrix A is **diagonalizable** if some S exists such that A = SΛS⁻¹
- Diagonalization makes computing powers of A much easier:
  - Aⁿ = (SΛS⁻¹)(SΛS⁻¹)…(SΛS⁻¹) = **SΛⁿS⁻¹**
  - Λⁿ is easy to compute since it's just a diagonal matrix (raise each diagonal entry to the power n)

## Eigenvalues & Eigenvectors of Symmetric Matrices
- Two special properties when A is **symmetric**:
  1. All eigenvalues of A are **real** (never complex)
  2. Eigenvectors are **orthonormal** — meaning matrix S is orthogonal, so **A = SΛSᵀ**
- **Definiteness** of a symmetric matrix depends only on the sign of its eigenvalues:
  - xᵀAx = xᵀSΛSᵀx = yᵀΛy = Σλᵢyᵢ²
  - Since yᵢ² ≥ 0 always, the sign of the whole expression depends entirely on the λᵢ's
  - Example: if all λᵢ > 0, then A is **positive definite**

## Eigenvalues of a PSD Matrix
- If A is **positive semi-definite (PSD)**, then for any eigenvector x⃗ of A:
  - x⃗ᵀAx⃗ ≥ 0 → λx⃗ᵀx⃗ ≥ 0 → λ‖x⃗‖² ≥ 0
- Since ‖x⃗‖² is always ≥ 0, this means **λ ≥ 0**
- **Conclusion:** all eigenvalues of a PSD matrix are non-negative

## Singular Value Decomposition (SVD)
- Diagonalization only works for **square** matrices. SVD is the equivalent tool for **rectangular** matrices (e.g., a Document-Term matrix)
- Instead of one set of eigenvectors, SVD uses two: **left singular vectors** and **right singular vectors**
- **SVD formula: A = UΣVᵀ**, where U is (m×m), Σ is (m×n), V is (n×n)

**What each piece means:**
- **U:** columns are the eigenvectors of AAᵀ (the *left* singular vectors)
- **V:** columns are the eigenvectors of AᵀA (the *right* singular vectors)
- **Σ:** a rectangular diagonal matrix, where each entry is the square root of an eigenvalue of AAᵀ (or AᵀA)

**Why it matters:** SVD lets us build a **lower-rank approximation** of a rectangular matrix — just keep the top *r* singular values in Σ along with the matching columns in U and rows in Vᵀ. This is the basis of dimensionality-reduction techniques.

## Matrix Calculus

### The Gradient
- For a function f : ℝ^(m×n) → ℝ, the **gradient** ∇_A f(A) is the matrix of partial derivatives w.r.t. every element of A:
  (∇_A f(A))ᵢⱼ = ∂f(A)/∂A_ij

### The Hessian
- For a function f : ℝⁿ → ℝ, the **Hessian** ∇²_x f(x) (or H) is the n×n matrix of second partial derivatives:
  (∇²_x f(x))ᵢⱼ = ∂²f(x)/∂xᵢ∂xⱼ
- The Hessian is always **symmetric**
- Note: the Hessian is *not* literally "the gradient of the gradient" (you can't take a gradient of a vector) — but if you take elementwise gradients of every element of the gradient vector, you effectively build the Hessian

## Differentiating Linear and Quadratic Functions

### Linear case: f(x) = bᵀx
- f(x) = Σ bᵢxᵢ
- ∂f(x)/∂x_k = b_k
- So **∇f(x) = b** — same intuition as differentiating f(x) = ax w.r.t. x when a, x are scalars, which just gives a

### Quadratic case: f(x) = xᵀAx (A symmetric)
- f(x) = ΣᵢΣⱼ Aᵢⱼxᵢxⱼ
- Differentiating step by step w.r.t. x_k eventually gives:
  ∂f(x)/∂x_k = 2·Σᵢ A_ki·xᵢ
- So **∇_x(xᵀAx) = 2Ax**

### Hessian of the quadratic form
- Differentiating ∇f(x) = 2Ax again w.r.t. x_l:
  ∂/∂x_k [∂f(x)/∂x_l] = 2A_kl
- So **∇²_x(xᵀAx) = 2A**
