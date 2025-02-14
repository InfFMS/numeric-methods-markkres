n1,n2=map(int,input().split())
a1,b1=map(int,input().split())
a2,b2=map(int,input().split())
def f(x):
    return (b1**2+(a1-x)**2)*n1+(b2**2+(a2+x)**2)*n2
if a1<a2:
    a=a1
    b=a2
else:
    a=a2
    b=a1
while b-a>0.001:
    c=(a+b)/2
    if f(a)*f(c)<=0:
        b=c
    else:
        a=c
print(f(a))
