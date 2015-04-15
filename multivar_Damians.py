import pandas as pd


# load the data file
# we skip row 1 because it's a note that affects our headers.
# we only grab 235,629 rows because the last two rows are a single description 
#  in column 0.
# try it without each and see what happens.
dfLoanData = pd.read_csv('LoanStats3c.csv', skiprows=1, nrows=235629)

# It should still yell at us that the column 19 (aka 'desc') is also mixed type.
# so we drop that column - we're not using it anyway.
dfLoanData = dfLoanData.drop('desc', axis=1)

# now we're ready to start thinking about the regression.
# first: interest rate is a string with a '%' symbol in it.
# use code you've already written to handle that.

# Income is already numeric, so you'll be fine there. You can begin to model 
#   that now.

# your first regression equation should be of the form:
# interest = intercept + constant1 * income

# use statsmodels and the same technique you used in the earlier linear 
# regression to solve.


# next one is home ownership. These are categorical variables, so you need to
# code them from string to numeric. Easiest way to do that is pandas categorical
# functions.
dfLoanData['home_ownership_code'] = pd.Categorical(dfLoanData['home_ownership']).codes

# so your next two regression equations are:
# interest = intercept + constant1 * income + constant2 * home_ownership

# and

# interest = intercept + constant1 * income + constant2 * home_ownership + constant3 * (annual income * home ownership)