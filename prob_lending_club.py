import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
print loansData[0:0]
loansData.dropna(inplace=True)

#Generate the boxplot
loansData.boxplot(column='Amount.Requested')
plt.title("Boxplot of Amount.Requested")
plt.savefig("Box_Amount_Requested")
plt.show()
#Generate the histogram
loansData.hist(column='Amount.Requested')
plt.title("Histogram of Amount.Requested")
plt.savefig("Hist_Amount_Requested")
plt.show()
#Generate the QQ plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist="norm", plot=plt)
plt.title("QQ plot of Amount.Requested")
plt.savefig("QQ_Amount_Requested")
plt.show()

print "Although the median amount invested and borrowed is the same, the"
print "overall amount funded by investors is slightly less than the amount requested."
print "This can be seen by comparing the boxplots of the two datasets:"

loansData.boxplot(column=['Amount.Requested','Amount.Funded.By.Investors'])
plt.title("Boxplot of Amount.Requested and Amount.Funded.By.Investors")
plt.savefig("Box_Amt_Req_and_Funded")
plt.show()

print "Some of the more credit-worthy borrowers who requested higher amounts"
print "received funding, thus there are more outliers in the higher end of the range."