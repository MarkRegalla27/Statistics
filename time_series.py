import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import scatter_matrix
from scipy import stats
import numpy as np
import statsmodels.api as sm
from sklearn.cross_validation import train_test_split

#loansData = pd.read_csv('LoanStats3c.csv')  #skiprows argument skips indicated row
#loansData = pd.read_csv('/users/markregalla/projects/LoanStats3b.csv', skiprows=1)
loansData = pd.read_csv('/users/markregalla/projects/LoanStats3b.csv', header=1, low_memory=False)
#loansData = loansData.drop('desc', axis=1)

# convert string to datetime object in pandas
loansData['issue_d_format'] = pd.to_datetime(loansData['issue_d']) 
dfts = loansData.set_index('issue_d_format') 
year_month_summary = dfts.groupby(lambda x : x.year * 100 + x.month).count()
loan_count_summary = year_month_summary['issue_d']

column_names = loansData.columns.tolist()
column_names = np.matrix(column_names).transpose()
#print column_names
#print year_month_summary	#24 rows x 52 columns
print loan_count_summary
#print dfts					#188125 rows x 52 columns
#print loansData['issue_d_format']

'''
X = np.matrix(year_month_summary).transpose()
Y = np.matrix(loan_count_summary).transpose()
X = sm.add_constant(X)
model = sm.OLS(Y,X)
f = model.fit()
'''

#plt.figure()
#plt.plot(loan_count_summary, year_month_summary, 'r.')
#plt.plot(loan_count_summary, 'r.')
#plt.show()

acf_plot = plt.figure()
acf_plot = sm.graphics.tsa.plot_acf(loan_count_summary)
acf_plot.savefig('acf.png')

pacf_plot = plt.figure()
pacf_plot = sm.graphics.tsa.plot_pacf(loan_count_summary)
pacf_plot.savefig('pacf.png')

print 'Open acf.png and pacf.png in the working directory to view the plots.'

#print f.summary()



