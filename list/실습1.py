def createListFromInput(n):
    lst = []
    for i in range(n):
        num = int(input("정수를 입력하세요: "))
        lst.append(num)
    return lst

lst1 = createListFromInput(5)
print(lst1) # 리스트를 확인차 출력

for n in lst1:
    print(n) # 요소 출력
