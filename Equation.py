import math
def f_perv(x):
    #return x**3-x+1
    #return x**2-2.7118281828**x
    return math.cos(x)+2*x-3
def f(x):
    if f_perv(-10)>f_perv(10):
        return -f_perv(x)
    else:
        return f_perv(x)
L=-5
R=5
D=0.001
while R-L>D:
    M=(R+L)/2
    if f(M)>0:
        R=M
    elif f(M)<0:
        L=M
print(M)
