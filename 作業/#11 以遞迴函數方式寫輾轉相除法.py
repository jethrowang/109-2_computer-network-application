def F(n,m):
    if n%m==0:
        return m
    else:
        return F(m,n%m)
x=F(36,128)
print(x)