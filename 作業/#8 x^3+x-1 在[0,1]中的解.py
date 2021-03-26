up,low=1,0
while up-low>0.000001:
    medium=(up+low)/2
    if medium**3+medium-1>0:
        up=medium
    if medium**3+medium-1<0:
        low=medium
    print(medium)