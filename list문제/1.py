'''
a = [1, 2, 3, 4]
a.append(a)
print(a)
# [1, 2, 3, 4, [...]]
'''
'''
a = [1, 2, 3, 4]
a.pop(3) # remove는 값 pop은 index
print(a)
'''
'''
numbers = [2000, 100]

for num in numbers:
    temp = num
    ans = 0
    while temp:
       temp //= 10
       ans += 1
    
    print(ans, num)
'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(numbers) // 2):
    j = 2*i+1
    numbers[j] = numbers[j] ** 2
    
print(numbers)

'''
d = {'name':"구름"}
d.clear()
print(d)
'''
'''
# tuple은 clear 안 됨
t = 1,2 ,34
t = ()
print(t)
'''
'''
numbers = [ 1, 2, 3, 4, 1, 1, 5, 5, 5]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] += 1
    else: 
        counter[num] = 1
        
print(counter)
'''
'''
n=5
for line in range(1, n+1):
    for blank in range(n - line):
        print(" ", end ="")
    for star in range(2*line-1):
        print("*", end ="")
    print()
'''
numbers = [ 1, 2, 3, 4, 1, 1, 5, 5, 5, 6]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] += 1
    else: 
        counter[num] = 1
        
print(len(counter))

    