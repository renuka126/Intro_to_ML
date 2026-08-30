# Supervised Learning

## Definition

Learning a function `f: X → Y` from a dataset of (input, output) pairs, where the output is already known (labeled). The model's job is to generalize this mapping to new, unseen inputs.

## The two big tasks

- **Regression** — output is continuous (e.g., predicting a price, a temperature)
- **Classification** — output is discrete/categorical (e.g., spam vs not spam)

## How it works (high level)

1. Collect labeled training data `{(x1, y1), (x2, y2), ..., (xn, yn)}`
2. Choose a model/hypothesis class (linear model, decision tree, neural net, etc.)
3. Define a loss function that measures how wrong a prediction is
4. Optimize model parameters to minimize loss on training data
5. Check performance on unseen (test) data — this is what actually matters

## Key idea I want to remember

Fitting training data well is not the goal — generalizing to new data is. A model that memorizes training data perfectly but fails on new data is useless (this connects directly to bias-variance later).

## My own example

Predicting whether a student will pass or fail based on attendance and assignment scores — that's classification. Predicting their exact marks out of 100 — that's regression.

## Questions to revisit

- How do you pick the right hypothesis class before knowing the true relationship in the data?