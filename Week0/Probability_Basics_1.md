# Probability Basics — Week 1 Tutorial 1
*NPTEL: Introduction to Machine Learning (Balaraman Ravindran)*

## Sample Space
- **Sample space (Ω):** set of all possible outcomes of an experiment
- Individual elements denoted by ω, called **elementary outcomes**
- Examples:
  - **Finite:** single die roll → Ω = {1,2,3,4,5,6}
  - **Countable:** infinite coin tosses until 5 consecutive heads → Ω = {H,T}^∞
  - **Uncountable:** speed of a vehicle measured with infinite precision → Ω = ℝ

## Event
- **Event:** any collection of possible outcomes — i.e., any subset of Ω
- Example: rolling a die → even event E = {2,4,6}, odd event O = {1,3,5}

## Set Operations
- A ⊂ B ⇔ x ∈ A ⇒ x ∈ B
- A = B ⇔ A ⊂ B and B ⊂ A
- A ∪ B = {x : x ∈ A or x ∈ B}
- A ∩ B = {x : x ∈ A and x ∈ B}
- Aᶜ = {x : x ∉ A}

## Set Algebra Laws
**Commutativity**
- A ∪ B = B ∪ A
- A ∩ B = B ∩ A

**Associativity**
- A ∪ (B ∪ C) = (A ∪ B) ∪ C
- A ∩ (B ∩ C) = (A ∩ B) ∩ C

**Distributivity**
- A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)

**DeMorgan's Laws**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ

## Disjoint Events
- Events A and B are **disjoint (mutually exclusive)** if A ∩ B = φ
- A sequence A₁, A₂, A₃, … is **pair-wise disjoint** if Aᵢ ∩ Aⱼ = φ for all i ≠ j

## Partition
- If A₁, A₂, … are pair-wise disjoint and ∪ᵢ₌₁^∞ Aᵢ = Ω, the collection forms a **partition** of Ω

## σ-Algebra
Given sample space Ω, a **σ-algebra** F is a collection of subsets of Ω satisfying:
- (a) Φ ∈ F
- (b) If A ∈ F, then Aᶜ ∈ F
- (c) If Aᵢ ∈ F for every i ∈ ℕ, then ∪ᵢ₌₁^∞ Aᵢ ∈ F

A set A ∈ F is called an **F-measurable set (event)**.

**Example:** Ω = {1,2,3}
- F₁ = {φ, {1}, {2}, {3}, {1,2}, {1,3}, {2,3}, {1,2,3}}
- F₂ = {φ, {1,2,3}}

### Sample Space Size Considerations
- For any Ω (countable or uncountable), 2^Ω is always a σ-algebra
- Example: Ω = {H,T} → power set F = {φ, {H}, {T}, {H,T}}
- If Ω is uncountable, probabilities **cannot** be assigned to every subset of 2^Ω

## Probability Measure
A probability measure P on (Ω, F) is a function P : F → [0,1] satisfying:
- (a) P(φ) = 0, P(Ω) = 1
- (b) If A₁, A₂, … are pair-wise disjoint members of F, then P(∪ᵢ₌₁^∞ Aᵢ) = Σᵢ₌₁^∞ P(Aᵢ)

**Example:** Rolling a die, identifying whether outcome is prime
- Ω = {1,2,3,4,5,6}
- F = {φ, {1,4,6}, {2,3,5}, {1,2,3,4,5,6}}
- P(φ) = 0, P({1,4,6}) = 0.5, P({2,3,5}) = 0.5, P(Ω) = 1

## Bonferroni's Inequality
- P(A ∩ B) ≥ P(A) + P(B) − 1
- General form: P(∩ᵢ₌₁ⁿ Aᵢ) ≥ Σᵢ₌₁ⁿ P(Aᵢ) − (n−1)
- Gives a **lower bound** on intersection probability — useful when hard to calculate directly
- Only useful when individual event probabilities are sufficiently large

## Boole's Inequality
- P(∪ᵢ₌₁^∞ Aᵢ) ≤ Σᵢ₌₁^∞ P(Aᵢ), for any sets A₁, A₂, …
- Gives a useful **upper bound** for the probability of the union of events

## Conditional Probability
- Given events A, B with P(B) > 0:
  P(A|B) = P(A∩B) / P(B)
- Since B has occurred, it becomes the **new sample space**
- Useful for updating beliefs/predictions once an event is observed

**Example:** A fair coin is tossed twice. Find P(both heads | at least one head).
- Ω = {HH, TT, HT, TH}, each with P = 1/4
- P(HH | at least one H) = P(HH ∩ (HT∪TH∪HH)) / P(HT∪TH∪HH) = P(HH) / P(HT∪TH∪HH)

## Bayes' Rule
Derivation:
- P(A|B) = P(A∩B)/P(B) → P(A∩B) = P(A|B)P(B)
- P(A∩B) = P(B|A)P(A)
- So P(A|B)P(B) = P(B|A)P(A)
- **P(A|B) = [P(B|A)·P(A)] / P(B)** (Bayes' Rule)

**General form (partition):** If A₁, A₂, … partition the sample space, and B is any subset:
P(Aᵢ|B) = [P(B|Aᵢ)·P(Aᵢ)] / Σⱼ P(B|Aⱼ)·P(Aⱼ)

- Lets us compute P(A|B) from the "inverse" conditional probability P(B|A)

**Example:** A student either knows (prob p) or guesses (prob q) the answer to an MCQ.
- K = student knows the answer, C = answers correctly
- P(K)=p, P(¬K)=1−p, P(C|K)=1, P(C|¬K)=q
- P(K|C) = P(C|K)P(K) / [P(K)P(C|K) + P(¬K)P(C|¬K)] = **p / (p + q(1−p))**

## Independent Events
- A and B are **independent** if P(A ∩ B) = P(A)·P(B)
- More generally, family {Aᵢ : i ∈ I} is independent if
  P(∩ᵢ∈J Aᵢ) = Πᵢ∈J P(Aᵢ) for all finite subsets J of I
- **Note:** pair-wise independence does **not** imply (full) independence

## Conditional Independence
Let A, B, C be events with P(C) > 0. A and B are **conditionally independent given C** if:
- P(A ∩ B | C) = P(A|C)·P(B|C)
- Equivalently: P(A | B∩C) = P(A|C)
