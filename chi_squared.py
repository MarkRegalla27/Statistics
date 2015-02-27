import matplotlib.pyplot as plt
import collections
import pandas as pd
import scipy.stats as stats
#from scipy import stats


# Load the reduced version of the Lending Club Dataset
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# Drop null rows
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
loansData.hist(column='Open.CREDIT.Lines')

chi, p = stats.chisquare(freq.values())
print "The chi squared value for the Open.CREDIT.Lines dataset is " + str(chi) + "."
#s = "The p-value is %1.5f" % p + "."
print("The p-value is %1.5f" % p + ".")
#plt.show()