import pandas as pd
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
#print loansData['Interest.Rate'][0:5]
print loansData['Loan.Length'][0:5]
