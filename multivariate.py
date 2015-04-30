import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.cross_validation import train_test_split

#loansData = pd.read_csv('LoanStats3c.csv')  #skiprows argument skips indicated row
loansData = pd.read_csv('/users/markregalla/projects/LoanStats3c.csv', skiprows=1, nrows=235629)  #skiprows argument skips indicated row
loansData = loansData.drop('desc', axis=1)


loansData['int_rate'] = loansData['int_rate'].map(lambda percent: round(float(percent.rstrip('%')),4) / 100)
#loansData['int_rate'] = loansData.apply(lambda x: pd.Series(x['int_rate'].rstrip('%')).astype('float'), axis=1)
#loansData['home_ownership_code'] = pd.Categorical(loansData['home_ownership']).code()

anninc = loansData['annual_inc']	#x value in regression
intrate = loansData['int_rate']		#y value in regression

x1 = np.matrix(anninc).transpose()
y = np.matrix(intrate).transpose()

X = sm.add_constant(x1)
model = sm.OLS(y,X).fit()
#f = model.fit()

a1 = model.params[1:2]
b =  model.params[0]

plt.figure()
plt.plot(anninc, intrate, 'r.')
plt.plot(anninc, b + a1*anninc, '-')
plt.xlabel('Annual Income')
plt.ylabel('Interest Rate')
plt.axis([0,500000,0,.35])		#plt.axis([min(x), max(x), min(y), max(y)])
#plt.show()

#print model.summary()

print 'Model Interest Rate on Home ownership'
print ''

dfdummies = pd.get_dummies(loansData['home_ownership'])
loansData = pd.merge(loansData, dfdummies, left_index=True, right_index=True)
#print dfdummies

#Model interest rate with home ownership using a logistic regression

X = loansData[['annual_inc','MORTGAGE','RENT','OWN']]
y = loansData['int_rate']
#logit = sm.Logit(y, X)
result = sm.Logit(y, X).fit()
#result = logit.fit()
#print result.summary()
coeff = result.params
print coeff

print "confidence interval"
print result.conf_int()

print "odds ratios"
print np.exp(result.params)

print "odds ratios and 95% confidence intervals"
params = result.params
conf = result.conf_int()
conf['OR'] = params
conf.columns = ['2.5%', '97.5%', 'OR']
print np.exp(conf)

#Introduce annual income on home ownership
print 'Introduce Annual Income'
print ''

sample_size = int(len(loansData) * .1)		#Use 10% of the data as a training set.  It makes the calculations faster to run and helps to prevent overfitting
index_list = np.random.choice(loansData.index.tolist(), sample_size)	#takes random sample of data

dfLoanDataSampled = loansData.loc[index_list]
dfLoanDataSampled = dfLoanDataSampled[['annual_inc', 'int_rate', 'home_ownership']]

trainData, testData = train_test_split(dfLoanDataSampled, test_size=0.2)	#returns two dataframes, the train and test sets
print 'train data'
column_names = dfLoanDataSampled.columns.tolist()

dftrainData = pd.DataFrame(trainData, columns=column_names)  #Assigns the training data set to dftrainData
dfDummies = pd.get_dummies(dftrainData['home_ownership'])
dftrainData = pd.merge(dftrainData, dfDummies, left_index=True, right_index=True)

#trainData['income_ANY'] = trainData.apply(lambda x: x['annual_inc'] * x['ANY'], axis = 1)
dftrainData['income_MORTGAGE'] = dftrainData.apply(lambda x: x['annual_inc'] * x['MORTGAGE'], axis = 1)
dftrainData['income_OWN'] = dftrainData.apply(lambda x: x['annual_inc'] * x['OWN'], axis = 1)
dftrainData['income_RENT'] = dftrainData.apply(lambda x: x['annual_inc'] * x['RENT'], axis = 1)

'''
loansData['income_ANY'] = loansData.apply(lambda x: x['annual_inc'] * x['ANY'], axis = 1)
loansData['income_MORTGAGE'] = loansData.apply(lambda x: x['annual_inc'] * x['MORTGAGE'], axis = 1)
loansData['income_OWN'] = loansData.apply(lambda x: x['annual_inc'] * x['OWN'], axis = 1)
loansData['income_RENT'] = loansData.apply(lambda x: x['annual_inc'] * x['RENT'], axis = 1)
'''

X2 = dftrainData[['income_MORTGAGE', 'income_RENT', 'income_OWN']]
y = dftrainData['int_rate']

Logit2 = sm.Logit(y, X2)
result2 = Logit2.fit()
#print result2.summary()

print "confidence interval"
print result2.conf_int()

print "odds ratios"
print np.exp(result2.params)

print "odds ratios and 95% confidence intervals"
params2 = result2.params
conf2 = result2.conf_int()
conf2['OR'] = params
conf2.columns = ['2.5%', '97.5%', 'OR']
print np.exp(conf2)

print 'There is little change in the odds ratios of predicting interest rates when'
print 'home ownership is taken into consideration.'
