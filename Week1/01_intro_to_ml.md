# Introduction to Machine Learning

## What it is

Machine Learning is about building systems that learn patterns from data instead of being explicitly programmed with rules for every case. Instead of writing `if-else` logic by hand, we give the system examples and let it figure out the mapping itself.

## Why it matters

Traditional programming breaks down when:
- The rules are too complex to hand-write (e.g., recognizing handwriting)
- The rules keep changing over time (e.g., spam patterns)
- We don't fully understand the rules ourselves (e.g., disease diagnosis from symptoms)

ML shifts the work from "write the rules" to "collect good data and let the model find the rules."

## The three main paradigms

| Type | Data | Goal |
|---|---|---|
| Supervised | Labeled (input + correct output) | Predict output for new inputs |
| Unsupervised | Unlabeled | Discover hidden structure |
| Reinforcement | No fixed dataset — agent + environment | Maximize long-term reward |

## My own example

Trying to predict rent prices in my area:
- Supervised: given past listings (features → actual rent), predict rent for a new flat
- Unsupervised: group listings into "types" of housing without knowing categories beforehand
- Reinforcement: not a great fit here — RL suits sequential decisions, not one-shot prediction

## Questions to revisit

- Where's the line between unsupervised learning and just "statistics"?
- How much labeled data is "enough" for supervised learning to work well?