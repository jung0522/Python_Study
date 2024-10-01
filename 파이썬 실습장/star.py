n = int(input("별을 세어보아요: "))

for line in range (1, n+1): 
   for blank in range(n-line, 0, -1):
     print(f" ", end = "")
   print( "*" * (2*line-1), end = "")
   print("")

   
for line in range (n+1, 2*n):
    for blank in range(line-n, 0, -1):
           print(f" ", end = "")   
    print("*"*(2*(n-(line-n))-1), end ="")
    print("")
    


   