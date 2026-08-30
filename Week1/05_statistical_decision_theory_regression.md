# Statistical Decision Theory - Regression

## The core idea

This gives a formal, mathematical way to answer: "what is the *best possible* prediction function, given uncertainty in the data?"

## Loss function

We measure how wrong a prediction is using a loss function. For regression, the most common is **squared error loss**:

L(y, f(x)) = (y - f(x))^2

## Expected prediction error

We want to minimize the *expected* loss over the true (unknown) data distribution:

EPE(f) = E[(Y - f(X))^2]

## The optimal predictor

For squared error loss, the function that minimizes expected loss is the **conditional mean**:

f*(x) = E[Y | X = x]

This means: the best possible prediction at a given input is the average of all possible outputs at that input.

## Why this matters practically

We can't compute the true conditional mean (we don't know the real distribution), so all regression models (linear regression, etc.) are really just *estimates* of this ideal function using the data we have.

## My own example

If predicting a student's exam score from hours studied, the "true" best prediction at 5 hours studied is the average score of *all* students (in the whole population) who studied exactly 5 hours — we're just trying to estimate that average from a limited sample.

## Questions to revisit

- Why is squared error the default choice — what changes if we use absolute error instead?