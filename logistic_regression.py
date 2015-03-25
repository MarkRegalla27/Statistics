import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove the "%" symbol from the interest rate data
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))
'''i = 1
print loansData['Interest.Rate'][:i]
if loansData['Interest.Rate'][:i] > 12:
	print 'yes'
'''
#Remove the word "months" from the Loan Length data
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda term: int(term.rstrip(' months')))

#Split the FICO Range into 2 separate values, and assign the lower of the 2 to FICO.Min
loansData['FICO.Min'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)

#Add column indicating whether interest rate is greater than 12%
loansData['Low.Interest.Flag'] = 0
loansData.ix[(loansData['Interest.Rate'] <= 12),'Low.Interest.Flag'] = 1
print loansData['Low.Interest.Flag'].value_counts()

#loansData['Less.Than.12'] = [loansData['Less.Than.12'].bool() for line in loansData['Interest.Rate'] if loansData['Interest.Rate'] < 12]
'''i = 0
for i in loansData:
	if [loansData['Interest.Rate'][0:i] < 12]:
		loansData['Less.Than.12'][0:i] = True
	else:
		loansData['Less.Than.12'][0:i] = False
'''
#df[df['Interest.Rate'] == 10].head() # should all be True
#df[df['Interest.Rate'] == 13].head() # should all be False
#loansData['Greater.Than.12']= loansData['Interest.Rate'].map(lambda x: if loansData['Interest.rate'] < 12: loansData['Greater.Than.12'] = True 

loansData['Intercept'] = 1.0
#print loansData['Intercept'][0:5]

#ind_vars just a list

#Website on functional programming:
#https://docs.python.org/2/howto/functional.html