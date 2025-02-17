import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("data.csv",usecols=[0],nrows=11)
I=data.iloc[:,0].tolist()
data=pd.read_csv("data.csv",usecols=[1],nrows=11)
U=data.iloc[:,0].tolist()
A,B=0,0
for i in range(len(U)):
    B+=U[i]*I[i]
    A+=I[i]**2
k=B/A
print(k)
plt.plot(U,I,'ro-')
plt.show()
