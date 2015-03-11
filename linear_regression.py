import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np 

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))
#print percent[0:5]

#print loansData['Loan.Length'][0:5]

loansData['Loan.Length'] = loansData['Loan.Length'].map(lambda term: int(term.rstrip(' months')))
print loansData.head()
print loansData.dtypes

#print term[0:5]
#print type(term[0:5].values[0][0])

#cleanFICORange = loansData.apply(lambda x: int(x['FICO.Range'].split('-')[0:1],axis=1))
#cleanFICORange = loansData['FICO.Range'].map(lambda x: x.split('-')[0:1])
#cleanFICORange = cleanFICORange.map(lambda cleanFICORange: [int(n) for n in cleanFICORange])
#print cleanFICORange[0:5]
#print cleanFICORange[0:5].values[1][0]
#print type(cleanFICORange[0:5].values[1][0])
#pd.series(bin.split('-')[0:2])

#cleanFICORange.hist(column=cleanFICORange)
#plt.show()

loansData['FICO.Min'] = loansData.apply(lambda x: pd.Series(x['FICO.Range'].split('-')[0:1]).astype('int'), axis=1)
#Series is an indexed 1 dimensional list in pandas, like an array in other languages
#loansData['FICO.Min'] = loansData['FICO.Min'].map(lambda y: [int(n) for n in y])
#print "FICO.Min"
print loansData['FICO.Min'][0:5]
#print type(loansData['FICO.Min'][0:5].values[0][0])	#values[row index][column index]

#plt.figure()
#loansData.hist(column='FICO.Min')
#plt.show()
#i = 0
#for i in cleanFICORange:
#	loansData['FICO.Score'] = cleanFICORange.values[i][0]

#loansData['FICO.Score'] = cleanFICORange
#print loansData['FICO.Score'][0:5]
#
scatter_matrix(loansData, alpha=0.05, figsize=(10,10))  #prints only numerical values in dataframe, not objects/strings
plt.show()

#from notebook
#matplotlib inline
#loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#plt.figure()
#p = scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
#plt.show()
