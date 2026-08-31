# Linear Regression

## Definition
Linear Regression is a **supervised learning algorithm** used to model the relationship
between a dependent variable (target, `y`) and one independent variable (feature, `x`)
by fitting a straight line through the data.

## The Model
$$
\hat{y} = \beta_0 + \beta_1 x + \epsilon
$$

- $\hat{y}$ — predicted value
- $\beta_0$ — intercept (value of y when x = 0)
- $\beta_1$ — slope (change in y per unit change in x)
- $\epsilon$ — irreducible error / noise

## Objective — Ordinary Least Squares (OLS)
We choose $\beta_0, \beta_1$ to **minimize the sum of squared residuals**:

$$
J(\beta_0, \beta_1) = \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
$$

Closed-form solution:
$$
\beta_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \qquad
\beta_0 = \bar{y} - \beta_1 \bar{x}
$$

## Key Assumptions
1. **Linearity** — relationship between x and y is linear
2. **Independence** — residuals are independent of each other
3. **Homoscedasticity** — constant variance of residuals
4. **Normality** — residuals are approximately normally distributed
5. **No/low multicollinearity** — relevant when extended to multiple predictors

## Evaluation Metrics
| Metric | Formula | Meaning |
|---|---|---|
| MSE | $\frac{1}{n}\sum(y_i-\hat{y}_i)^2$ | Average squared error |
| RMSE | $\sqrt{MSE}$ | Error in original units |
| MAE | $\frac{1}{n}\sum\|y_i-\hat{y}_i\|$ | Average absolute error |
| R² | $1 - \frac{SS_{res}}{SS_{tot}}$ | Proportion of variance explained |