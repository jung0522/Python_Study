# 22
factor_list=[]
def factor(n):
    for i in range(1, n+1):
        if(n % i == 0):
           factor_list.append(i)
           
    return factor_list

for n in range(2, 20+1):
    factor_list=[]
    count = len(factor(n))
    print(f"{n:2}의 약수 개수: {count}")
 

            
      