x=int(input("請輸入西元年分："))
if x%4==0 and x%100!=0 or x%400==0:
    print("閏年")
else:
    print("非閏年")