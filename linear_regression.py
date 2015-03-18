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
#loansData.hist(column='FICO.Min')
#plt.show()

#Produce the scatter matrix
#scatter_matrix(loansData, alpha=0.05, figsize=(10,10))  #prints only numerical values in dataframe, not objects/strings
#plt.show()

intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Min']

loansData['10K.Request']=10000
loansData['30K.Request']=30000

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

req10K = loansData['10K.Request']
x1_10K = np.matrix(fico).transpose()
x2_10K = np.matrix(req10K).transpose()
x_10K = np.column_stack([x1, x2_10K])
x_10K = sm.add_constant(x_10K)

plt.plot(fico, intrate, 'r.')	#plot a scatterplot where fico is the x-value, intrate is the y value, and 'r.' tells the points to be red dots
#plt.plot(fico, f.fittedmodel, 'b.', label='Fitted Values')
plt.xlabel('FICO Min')
plt.ylabel('Interest Rate')
plt.legend(loc="best")
plt.show()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared