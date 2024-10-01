
def gcd(n1, n2):
    max_gcd = 0
    if n1 >= n2:
        for i in range(1, n2+1): #1부터
            if ((n1 % i == 0) and (n2 % i == 0)):
                if i > max_gcd:
                    max_gcd = i
    else:
        for i in range(1, n1+1):
            if ((n1 % i == 0) and (n2 % i == 0)):
                if i > max_gcd:
                    max_gcd = i
    print(max_gcd)

              
def lcm(n1, n2):
    if n1 > n2:
        for j in range(n1, n1*n2+1):
            if ((j % n1  == 0) and (j % n2 == 0)):
                print(f"{j}", end = " ")
                break
    else:
        for j in range(n2, n1*n2+1): 
            if ((j % n1  == 0) and (j % n2 == 0)):
                print(f"{j}", end = " ")
                break
n1 = int(input("수1: "))
n2 = int(input("수2: "))

gcd(n1, n2)     
lcm(n1, n2)
  
