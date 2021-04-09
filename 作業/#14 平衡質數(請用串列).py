prime=[]
for n in range(2,1001):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
    if flag==1:
        prime.append(n)
balancedprime=[]
for n in range(1,len(prime)-2):
    if prime[n]==(prime[n-1]+prime[n+1])/2:
        balancedprime.append(prime[n])
print(balancedprime)