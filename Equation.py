import math
import matplotlib.pyplot as plt
import numpy as np

def f_perv(x):
    #return x**3-x+1
    #return x**2-2.7118281828**x
    return math.cos(x)+2*x-3
def f(x):
    if f_perv(L)>f_perv(R):
        return -f_perv(x)
    else:
        return f_perv(x)
L=int(input("Введите левую границу "))
R=int(input("Введите правую границу "))
x=np.linspace(L,R,300)
D=0.001
while R-L>D:
    M=(R+L)/2
    if f(M)>0:
        R=M
    elif f(M)<0:
        L=M
print(M)


y=[f(X) for X in x]
plt.plot(x,y)
plt.show()
