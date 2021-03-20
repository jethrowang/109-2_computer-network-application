def prime(x):
    for i in range(2,x):
        if x%i==0:
            return False
    return True
'''https://www.itread01.com/content/1541858906.html'''
def palindrome(x):
    if x<0 or (x != 0 and x%10==0):
        return False
    x_revers = 0
    while x_revers<x:
        x_revers = x_revers * 10 + x % 10
        x=x//10
        if x_revers==x:
            return True
    if x_revers==x or x_revers//10==x:
        return True
    return False
for n in range(2,10001):
    if prime(n) and palindrome(n):
        print(n)