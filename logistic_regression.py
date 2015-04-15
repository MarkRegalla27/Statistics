import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm
import math

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

#Remove the "%" symbol from the interest rate data
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))

#Remove the word "months" from the Loan Length data
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda term: int(term.rstrip(' months')))

#Split the FICO Range into 2 separate values, and assign the lower of the 2 to FICO.Min
loansData['FICO.Min'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)

#Add column indicating whether interest rate is greater than 12%
loansData['Low.Interest.Flag'] = 0
loansData.ix[(loansData['Interest.Rate'] <= 12),'Low.Interest.Flag'] = 1 	#index function
#print loansData['Low.Interest.Flag'].value_counts()

loansData['Intercept'] = 1.0
#print loansData.head()

#ind_vars just a list
ind_vars = ['Amount.Requested', 'FICO.Min', 'Intercept']

logit = sm.Logit(loansData['Low.Interest.Flag'], loansData[ind_vars])
result = logit.fit()
coeff = result.params
print coeff

#Create the linear model: interest_rate = b + a1(FICOScore) + a2(LoanAmount)
b = coeff[2]
a1 = coeff[1]
a2 = coeff[0]
print b, a1, a2

FICOScore = 720
LoanAmount = 10000

def logistic_function(FICOScore, LoanAmount, b, a1, a2):
	prob = 1 / (1+ math.e**(-b - a1 * FICOScore + a2 * LoanAmount))
	if prob > 0.7:
		awarded = 'The loan will be awarded.'
	else:
		awarded = 'The loan will not be awarded.'
	return prob, awarded

probResult, awarded = logistic_function(FICOScore, LoanAmount, b, a1, a2)
print probResult
print awarded

print 'Given the data provided, a borrower with a FICO Score of 720 has a ' + str(round(probResult*100, 2)) + '%'
print 'chance of obtaining a $10,000 loan with an interest rate < 12%.'
print 'We conclude that the loan will be awarded as the probability is above the '
print 'predefined threshold of 70%.'
