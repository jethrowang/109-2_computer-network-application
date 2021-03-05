x=3
y=3
z=3
if x+y>z:
    print("可圍成")
    if x**2+y**2>z**2:
        if x==y and y==z:
            print("正三角形")
        elif x==y or y==z:
            print("等腰銳角三角形")
        else:
            print("銳角三角形")
    if x**2+y**2==z**2:
        if x==y:
            print("等腰直角三角形")
        else:
            print("直角三角形")
    if x**2+y**2<z**2:
        if x==y:
            print("等腰鈍角三角形")
        else:
            print("鈍角三角形")
else:
    print("不可圍成三角形")