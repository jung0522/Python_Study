def recursive ( num ):
    for n in range (num, 0, -1):
        if(num == 1):
            return n
        else:
            return n + recursive(n-1)
        
        
print(recursive(100))