# Probability Basics — Week 1 Tutorial 1 (Part 2)
*NPTEL: Introduction to Machine Learning (Balaraman Ravindran)*

## Random Variable
- A **random variable** is a function X : Ω → ℝ — i.e., a function from the sample space to the real numbers
- Examples:
  - The sum of outcomes on rolling 3 dice
  - The number of heads observed when tossing a fair coin 3 times

## Induced Probability Function
- Let Ω = {ω₁, ω₂, …} be a sample space and P a probability measure
- Let X be a random variable with range 𝒳 = {x₁, x₂, …, xₘ}
- The **induced probability function** Pₓ on 𝒳:
  Pₓ(X = xᵢ) = P({ωⱼ ∈ Ω : X(ωⱼ) = xᵢ})

**Example:** Fair coin tossed 3 times, X = number of heads

| ω | HHH | HHT | HTH | THH | TTH | THT | HTT | TTT |
|---|---|---|---|---|---|---|---|---|
| X(ω) | 3 | 2 | 2 | 2 | 1 | 1 | 1 | 0 |

| x | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Pₓ(X=x) | 1/8 | 3/8 | 3/8 | 1/8 |

## Cumulative Distribution Function (CDF)
- The cdf of X, denoted Fₓ(x), is defined by: **Fₓ(x) = Pₓ(X ≤ x)**, for all x

**Example** (same coin-toss experiment):

| x | (−∞,0] | (−∞,1] | (−∞,2] | (−∞,3] | (−∞,∞) |
|---|---|---|---|---|---|
| Fₓ(x) | 1/8 | 1/2 | 7/8 | 1 | 1 |

**A function Fₓ(x) is a valid cdf iff:**
- **Monotonicity:** if x ≤ y, then Fₓ(x) ≤ Fₓ(y)
- **Limiting values:** lim(x→−∞) Fₓ(x) = 0 and lim(x→∞) Fₓ(x) = 1
- **Right-continuity:** for every x, lim(y↓x) Fₓ(y) = Fₓ(x)

## Continuous & Discrete Random Variables
- X is **continuous** if Fₓ(x) is a continuous function of x
- X is **discrete** if Fₓ(x) is a step function of x

## Probability Mass Function (PMF)
- For a discrete r.v. X: **fₓ(x) = P(X = x)**, for all x

**Example — Geometric r.v. with parameter p:**
fₓ(x) = (1−p)ˣ⁻¹p for x = 1,2,…; 0 otherwise

## Probability Density Function (PDF)
- For a continuous r.v. X, the pdf fₓ(x) satisfies: **Fₓ(x) = ∫₋∞ˣ fₓ(t) dt**, for all x
- **Properties:**
  - fₓ(x) ≥ 0, for all x
  - ∫₋∞^∞ fₓ(x) dx = 1

## Expectation
- The expected value (mean) of X, denoted E[X]:
  - **Continuous RV:** E[X] = ∫₋∞^∞ x·fₓ(x) dx
  - **Discrete RV:** E[X] = Σ x·fₓ(x) = Σ x·P(X=x)

**Example:** X ∈ {−2,−1,1,3} with P = {1/4, 1/8, 1/4, 3/8}. Find E[Y] where Y = X².
- Y takes values 1, 4, 9 with probabilities 3/8, 1/4, 3/8
- E(Y) = Σ y·P(Y=y) = 1·(3/8) + 4·(1/4) + 9·(3/8) = **19/4**
- Alternatively: E(Y) = E(X²) = Σ x²·P(X=x) = 4·(1/4)+1·(1/8)+1·(1/4)+9·(3/8) = **19/4**

## Properties of Expectations
Let X be a random variable, a, b, c constants, g₁(X) and g₂(X) functions whose expectations exist:
- E(a·g₁(X) + b·g₂(X) + c) = a·Eg₁(X) + b·Eg₂(X) + c
- If g₁(X) ≥ 0 for all x, then Eg₁(X) ≥ 0
- If g₁(X) ≥ g₂(X) for all x, then Eg₁(X) ≥ Eg₂(X)
- If a ≤ g₁(X) ≤ b for all x, then a ≤ Eg₁(X) ≤ b

## Moments
- **nth moment:** μₙ′ = E[Xⁿ]
- **nth central moment:** μₙ = E[(X − μ)ⁿ]

## Covariance
- cov(X, Y) = E[(X − EX)(Y − EY)]
- Measures how much two random variables change together
- **Large negative** → variables move oppositely; **near zero** → little linear relation; **large positive** → variables move together

## Correlation
- ρ(X, Y) = cov(X, Y) / √(var(X)·var(Y))
- **Notes:**
  - Requires individual variances to be non-zero and finite
  - ρ(X, Y) lies between −1 and +1

## Marginal Distributions
- Given joint PMF: fₓ,ᵧ(x, y) = P(X = x, Y = y)
- Marginal PMFs derived by summing over the other variable:
  - fₓ = Σᵧ fₓ,ᵧ(x, y) (marginal PMF of X)
  - fᵧ = Σₓ fₓ,ᵧ(x, y) (marginal PMF of Y)

## Conditional Distributions
- fₓ|ᵧ(x|y) = P(X = x | Y = y)
- Using conditional probability definition: **fₓ|ᵧ(x|y) = fₓ,ᵧ(x, y) / fᵧ(y)**
- Undefined if fᵧ(y) = 0

## Bernoulli Distribution
- X takes value 0 or 1:
  - fₓ(0) = P(X=0) = 1−p
  - fₓ(1) = P(X=1) = p  (0 ≤ p ≤ 1)
- **E[X] = p**, **var(X) = p(1−p)**

## Binomial Distribution
- n independent Bernoulli trials, probability of success p per trial
- X = number of successes in n trials:
  **P(X = x | n, p) = C(n,x)·pˣ·(1−p)ⁿ⁻ˣ**, where C(n,x) = n! / [(n−x)!x!], 0 ≤ x ≤ n
- **E[X] = np**, **var(X) = np(1−p)**

## Geometric Distribution
- Series of independent Bernoulli trials, each with success probability p
- X = number of trials before the first success:
  **P(X = x | p) = (1−p)ˣ⁻¹p**, x = 1, 2, 3, …
- **E[X] = 1/p**, **var(X) = (1−p)/p²**
