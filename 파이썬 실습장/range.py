n = 20
k = 30
count = 0
for i in range(n, n*k+1):
    if i % n == 0 and i % k == 0:
        print(i)
        break
    
