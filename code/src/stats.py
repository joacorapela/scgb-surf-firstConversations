
import statsmodels.api as sm

def linearRegressionAnalysis(x, y):
    regressors = sm.add_constant(x)
    fit = sm.OLS(endog=y, exog=regressors).fit()
    predicted = fit.params[0]+x*fit.params[1]
    p_value = fit.pvalues[1]

    return predicted, p_value
