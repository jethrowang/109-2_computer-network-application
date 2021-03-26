x=int(input("請輸入正整數："))
if x%2==0:
    print("考拉茲猜想的下一個數字：",x/2)
else:
    print("考拉茲猜想的下一個數字：",3*x+1)