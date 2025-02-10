import math
def f(x):
    return math.cos(x)
def pif(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
length=0
for i in range(0.001, math.pi+0.001, 0.001):
    length+=pif(i,f(i),i-0.001,f(i-0.001))
print(length)
