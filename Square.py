import math
import matplotlib.pyplot as plt
import numpy as np
def y1(x):
    return math.sin(2*x)+1
def y2(x):
    return -0.2*x**2+0.5
def f(x):
    return y1(x)-y2(x)
a=0
b=math.pi
i=a+0.001
S=0
while i<=b:
    S+=(f(i-0.001)+f(i))*0.001/2
    i+=0.001
print(S)
    
x=np.linspace(0,math.pi,300)
Y1=[y1(X) for X in x]
plt.plot(x,Y1)
Y2=[y2(X) for X in x]
plt.plot(x,Y2)
plt.fill_between(x,Y1,Y2)
plt.show()
