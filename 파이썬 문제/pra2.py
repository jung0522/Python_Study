list1 = [1, 2, 3, 4, 1, 2, 3, 1, 4, 1, 2, 3]

print(f"{list1}에서")
list1.sort()
dict1 = {}
count = 0

for i in list1:
    
    if i not in dict1:
        count = 1
        dict1[i] = count 
    else:
        count += 1
        dict1[i] = count   
   
print(f"사용된 숫자의 종류는 {len(dict1)}개입니다.")
print(f"참고: {dict1}")
