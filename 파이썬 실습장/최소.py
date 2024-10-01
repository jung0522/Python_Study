
def gcd (m, n):
    if  m == n:
        return m
    elif (m > n):
        return gcd(m-n, n)
    else:
        return gcd(m, n-m)
def lcd(m,n):
    return m*n

print(gcd(20,10))
print( lcd(20,15) // gcd(20,15))