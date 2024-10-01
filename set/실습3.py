import random
set1 = set()


while True:
    num = random.randint(1, 20)
    set1.add(num)
    if len(set1) == 10:
        break
    
print(set1)