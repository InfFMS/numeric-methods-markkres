import numpy
import matplotlib.pyplot as plt
import math

#Вводится система отсчета такая что при y>1 коэффициент преломления n1 в ином случае n2
#и (a1,b1) (a2,b2) координаты точек в декартовой системе координат и луч идет
#от(a1,b1) до (a1,b1)
n1,n2=map(float,input().split())
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
def f(x):
    return ((b1**2+(a1-x)**2)*n1+(b2**2+(a2-x)**2)*n2)**0.5
L, R=min(a1,a2), max(a1,a2)
tochnost=1e-6
while R-L>tochnost:
    m1=L+(R-L)/3
    m2=R-(R-L)/3
    if f(m1)<f(m2):
        R=m2
    else:
        L=m1
x_min=(L+R)/2

storona1=(a1-x_min)**2
storona2=(b1)**2
hipotinuse=math.sqrt(storona1+storona2)
alpha=math.asin(math.sqrt(storona1)/hipotinuse)

print(alpha)

plt.plot([a1,x_min],[b1,0],'ro-')
plt.plot([x_min,a2],[0,b2],'bo-')
plt.plot([a1,a2],[0,0],"black")
plt.show()
