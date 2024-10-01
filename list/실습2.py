def createDivisorsList(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)
    return lst

# 사용자로부터 정수 입력 받기
n = int(input("1000이하의 정수 한 개를 입력하세요: "))

# 약수 리스트 생성
lst = createDivisorsList(n)
print(lst) # 약수 리스트 확인을 위해 화면에 출력


# 약수의 합 구하기
sum = 0
for i in lst:
  sum += i
print(f"약수들의 총 합: {sum}") # 합계 출력
