def f(x):
    return x**3-x+1
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
