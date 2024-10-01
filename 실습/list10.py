x = (map(int, input("수를 입력하시오: ").split()))
print(x)
x = list(map(int, input("수를 입력하시오: ").split()))
print(x)
x, y, z = map(int, input("수를 입력하시오: ").split())
print(x, y, z)

# ['adfsdf']
string = input("문자열을 입력하시오: ").split()
print(string)

numbers = [1,2,3,4,5,6]
print("*".join(list(map(str, numbers))))

string = ["hello", "world"]
print("*".join(string))
