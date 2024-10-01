def createListFromInput(n):
    tup = ()
    for i in range(n):
        num = int(input("정수를 입력하세요: "))
        tup += (num, )
    return tup    

tup = createListFromInput(5)
print(tup) # 리스트를 확인차 출력

for n in tup:
    print(n) # 요소 출력
