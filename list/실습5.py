def funcReturnsTuple():
    return 1, 2

def funcReturnsList():
    return [3, 4, 5]

tuple1 = funcReturnsTuple()
list1 = funcReturnsList()
x, y = funcReturnsTuple()
a, b, c = funcReturnsList()

print(type(tuple1))
print(type(list1))
print(type(x))
print(type(a))

def orderNumbers(num1, num2):
    if num1 <= num2:
        return num1, num2
    else:
        return num2, num1

num1, num2 = orderNumbers(2130, 2140)

print(num1, num2)

num1, num2 = orderNumbers(100, 1)

print(num1, num2)

