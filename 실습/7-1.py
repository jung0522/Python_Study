max = 0
n = 5
while n:
    num = int(input("수를 입력하시오: "))
    if num > max:
        max = num
    n -= 1
print(max)