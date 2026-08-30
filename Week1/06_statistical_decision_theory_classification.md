# Statistical Decision Theory - Classification

## The core idea

Same decision-theory framework as regression, but now the output is a discrete class label instead of a continuous number.

## Loss function

The most common loss here is **0-1 loss**:

L(y, f(x)) = 0 if f(x) = y, else 1

It just penalizes being wrong — it doesn't care *how* wrong.

## The optimal classifier

Minimizing expected 0-1 loss leads to the **Bayes classifier**:

f*(x) = argmax_k P(Y = k | X = x)

In words: for a given input, pick the class with the highest posterior probability.

## Bayes error rate

Even the optimal (Bayes) classifier isn't always right — if classes genuinely overlap in feature space, there's an irreducible error rate called the **Bayes error rate**. No classifier can do better than this on that data.

## My own example

Classifying an email as spam or not spam — if a particular pattern of words appears in both spam and legitimate emails 50/50, no classifier (however good) can be 100% accurate on those cases. That's the Bayes error rate showing up.

## Questions to revisit

- How do real classifiers (like logistic regression) approximate the true posterior probability `P(Y|X)`?