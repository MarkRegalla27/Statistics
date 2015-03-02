import pandas as pd

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

percent = loansData['Interest.Rate'].map(lambda percent: round(float(percent.rstrip('%')),4))
#print percent[0:5]

#print loansData['Loan.Length'][0:5]

term = loansData['Loan.Length'].map(lambda term: term.rstrip(' months'))
#print term[0:5]

cleanFICORange = loansData['FICO.Range'].map(lambda cleanFICORange: cleanFICORange.split('-'))
cleanFICORange = cleanFICORange.map(lambda cleanFICORange: [int(n) for n in cleanFICORange])
print cleanFICORange[0:5]
print cleanFICORange[0:5].values[0][1]



#g = lambda x: 
