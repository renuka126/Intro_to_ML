# Calculus

This is the math behind how a model actually *learns* — every training loop is calculus in disguise.

## Core ideas

**Derivative** — the rate of change of a function. If loss goes down as a weight changes, the derivative tells you which direction and by how much.

**Partial derivatives** — a derivative with respect to one variable while holding the others fixed. Since models have thousands (or billions) of weights, we need a partial derivative for each one.

**Gradient** — the vector of all partial derivatives. It points in the direction of steepest increase of the loss function — so we move *opposite* to it during training (gradient descent).

**Chain rule** — lets you compute the derivative of a composed function by multiplying the derivatives of each piece. This is literally what backpropagation is: applying the chain rule layer by layer, from the output back to the input, to figure out how much each weight contributed to the error.

## Why it matters for ML

- Every "the model is learning" moment is a gradient descent step
- Backpropagation = chain rule applied systematically through a computation graph
- Understanding this is what separates "I called `.fit()`" from "I know why `.fit()` works"

## What's in the notebook

- Symbolic differentiation with `sympy` for a few example functions
- Manual gradient descent from scratch on `y = x²`, plotting the descent path
- A short comparison of learning rate too high vs too low vs just right
