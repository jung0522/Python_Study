numbers = [1,2,3,45,1,41,12,3,1,2,3,4,4,1,2,1,1,1,1,1,1,5]
d = {}

for i in numbers:
   
   if i not in d:
       d[i] = 1
   else:
       d[i] += 1
       
print(d)
       