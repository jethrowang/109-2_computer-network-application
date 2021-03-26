def F(n):
    print(n)
    if n==1:
        return
    if n%2==0:
        return F(n//2)
    else:
        return F(n*3+1)
F(50)