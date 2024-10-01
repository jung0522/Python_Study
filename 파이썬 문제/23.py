#23
list1 = [1, 5, 8, 10 ,14]
list2 = [2, 4, 5, 9]
 
def sortlist(list1, list2):
     newlist = []
     for i in list1:
         newlist.append(i)
         
     for i in list2:
        newlist.append(i)
        
     newlist.sort()
     
     return newlist
 
print(sortlist(list1, list2))
     