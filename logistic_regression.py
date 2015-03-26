import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#Remove the "%" symbol from the interest rate data
loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))

#Remove the word "months" from the Loan Length data
loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda term: int(term.rstrip(' months')))

#Split the FICO Range into 2 separate values, and assign the lower of the 2 to FICO.Min
loansData['FICO.Min'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)

#Add column indicating whether interest rate is greater than 12%
loansData['Low.Interest.Flag'] = 0
loansData.ix[(loansData['Interest.Rate'] <= 12),'Low.Interest.Flag'] = 1 	#index function
print loansData['Low.Interest.Flag'].value_counts()

loansData['Intercept'] = 1.0
#print loansData.head()
#print loansData['Intercept'][0:5]

#ind_vars just a list
ind_vars = ['Loan.Length', 'FICO.Min', 'Intercept']
print ind_vars
#print loansData.columns[1:]
#print loansData['ind_vars']

#logit = sm.Logit(loansData['Low.Interest.Flag'], loansData['ind_vars'])
#http://blog.yhathq.com/posts/logistic-regression-and-python.html