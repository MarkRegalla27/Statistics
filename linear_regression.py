import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove the "%" symbol from the interest rate data
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))
#print percent[0:5]

#Remove the word "months" from the Loan Length data
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda term: int(term.rstrip(' months')))

#Split the FICO Range into 2 separate values, and assign the lower of the 2 to FICO.Min
loansData['FICO.Min'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)
#Series is an indexed 1 dimensional list in pandas, like an array in other languages
#loansData['FICO.Min'] = loansData['FICO.Min'].map(lambda y: [int(n) for n in y])

#Plot a histogram of FICO.Min
loansData.hist(column='FICO.Min')
plt.show()

#Produce the scatter matrix
scatter_matrix(loansData, alpha=0.05, figsize=(10,10))  #prints only numerical values in dataframe, not objects/strings
plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Min']
req10K = 10000
req30K = 30000

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

#Stack x1 and x2 into one matrix
x = np.column_stack([x1,x2])

#Create the linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

a1, a2 = f.params[1:3]
b = f.params[0]

plt.plot(fico, intrate, 'r.')	#plots a scatterplot where fico is the x-value, intrate is the y value, and 'r.' tells the points to be red dots
plt.plot(fico, b + a1*fico + a2*10000, '-', label='$10000 Requested')	#plot linear fit of intrate vs fico where amount.requested = 10000
plt.plot(fico, b + a1*fico + a2*30000, '-', label='$30000 Requested')	#plot linear fit of intrate vs fico where amount.requested = 30000
plt.xlabel('FICO Min')
plt.ylabel('Interest Rate')
plt.legend(loc="best")
plt.show()


print 'Coefficients: ', f.params[1:3]
print 'Intercept: ', f.params[0]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared

print 'The P-value is less than 0.05, suggesting that the linear relationship of'
print 'Interest Rate and FICO score is not due to chance'