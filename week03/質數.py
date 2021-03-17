print("1~100的質數：")
for n in range(2,101):
    flag=1
    for i in range(2,n):
        if n%i==0:
            flag=0
    if flag==1:
        print(n)