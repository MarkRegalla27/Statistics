import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

#plots for testlist
testlist = [1, 4, 5, 6, 9, 9, 9]
c = collections.Counter(testlist)

# calculate the number of instances in testlist
count_sum = sum(c.values())

for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum) + " in testlist."
  
#print count_sum 
plt.boxplot(testlist)					#plots the boxplot for testlist
plt.title("Boxplot for Testlist")
plt.savefig("Testlist_Boxplot")
plt.show()
plt.hist(testlist, histtype='bar')		#plots the histogram for testlist
plt.title("Histogram for Testlist")
plt.savefig("Testlist_Histogram")
plt.show() 
plt.figure()  
graph1 = stats.probplot(testlist, dist="norm", plot=plt)
plt.title("QQ Plot for Testlist")
plt.savefig("Testlist_QQ")		#this will generate the QQ graph for testlist
plt.show() 								


#plots for x
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
b = collections.Counter(x)

# calculate the number of instances in x
count_sum2 = sum(b.values())
for j,w in b.iteritems():
  print "The frequency of number " + str(j) + " is " + str(float(w) / count_sum2) + " in x."

plt.boxplot(x)					#plots the boxplot for x
plt.title("Boxplot for x")
plt.savefig("x_boxplot")
plt.show()
plt.hist(x, histtype='bar')		#plots the histogram for x
plt.title("Histogram for x")
plt.savefig("x_histogram")
plt.show()
plt.figure()
graph = stats.probplot(x, dist="norm", plot=plt)
plt.title("QQ Plot for x")
plt.savefig("x_QQ")				#this will generate the QQ graph for x				
plt.show()