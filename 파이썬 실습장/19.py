def getWord (str, n):
    strlist = []
    strlist = str.split(' ')
    
    for i in range(len(strlist)):
        if ( n-1 == i  ):
            return strlist[i]
        
print(getWord("A beautiful day", 1))
print(getWord("A beautiful day", 3))
     