limit = 10

n=1
sum = 0
while(sum < limit):
    sum += n
    n += 1
    
print("%d를 더할 때 %d를 넘기고 그 때의 값은 %d이다." % (n-1, limit, sum))