import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
print loansData[0:0]
loansData.dropna(inplace=True)

#Generate the boxplot
loansData.boxplot(column='Amount.Requested')
plt.show()
#Generate the histogram
loansData.hist(column='Amount.Requested')
plt.show()
#Generate the QQ plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.show()


