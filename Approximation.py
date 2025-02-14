import pandas as pd
data=pd.read_csv("data.csv",usecols=[0],nrows=11)
I=data.iloc[:,0].tolist()
data=pd.read_csv("data.csv",usecols=[1],nrows=11)
U=data.iloc[:,0].tolist()
R=[U[i]/I[i] for i in range(0,10)]
print(sum(R)/len(R))
