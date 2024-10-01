
def reculsive (n):
    if ( n == 1):
        return 1
    else:
        return n * reculsive(n-1)
    
print(reculsive(5))
