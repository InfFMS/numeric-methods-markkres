import math
e=2.718281828
def tanh(x):
    return (e**(2*x)-1)/(e**(2*x)+1)
def f(x):
    #return math.cos(x)
    #return math.cos(x)+0.1*x**2
    return tanh(x-math.pi/2)
    #return -0.2*(x-math.pi)**3+0.5(x-math.pi)**2+1
def pif(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
length=0
i=0.001
while i<math.pi+0.001:
    length+=pif(i,f(i),i-0.001,f(i-0.001))
    i+=0.001
print(length)
