# print("성: 홍", "길동", sep = " 이름: ") 성: 홍 이름: 길동
"""
print("홍", "길", "동", sep = "\n")
홍
길
동
"""
"""
입력: 프로그램에서 처리하려고 하는 데이터
출력: 프로그램에서 처리된 후의 결과를 사용자에게 보여주는 것
순차: 순서에 따라 처리하는 과정. 일을 순서대로 나누어서 수행하는 과정.
조건: 경우에 따라 구분하여 처리하는 과정. 예를 들어 조건이 만족될 때에는 어떤 일을 해야 하고 조건이 만족되지 않을 때에는 다른 일을 해야 함
반복: 같은 일을 여러 번 다시 하는 과정
재사용: 프로그램의 일부를 고치지 않고 다시 활용하는 과정. 프로그래밍 언어의 용어를 빌리면 함수 등을 만들어서 코드를 재사용함
"""
"""
print("a"+"b")
print("ab"-"b") # 문자열 - 문자열 x
print("a"*3) aaa
"""
# print(" \\ \' \' \" \" %% ") \\ \' \"
# str(3 < 2) 'False'
#가나다" + "abc" * 2 '가나다abcabc'
# ("가나다" + "abc") * 2 '가나다abc가나다abc'
'''
파이썬에서는 변수 이름은 메모리 공간에 있는 숫자, 문자열, 객체(object)를 가리키는 이름표의 역할을 함
변수 이름표를 메모리 공간에 붙이는 것을 "변수가 메모리 공간 또는 메모리 공간에 있는 값을 참조(reference)한다"라고 함

'''

'''
파이썬의 변수 이름 짓기 규칙
이름 길이에 제한 없음
변수는 반드시 유니코드 문자나 ‘_’로 시작
문자나 '_'로 시작한 후에는 숫자도 사용 가능
변수 이름에 공백이 없어야 함
특수 문자 활용 불가
키워드(예약어)가 아니어야 함
대문자와 소문자를 다르게 구별함
좋은 예: a, a2, _a, MyVariable, __variable, myVariable
MyVariable과 myVariable은 다른 변수
나쁜 예: 2a, a$, My Variable, for
a정 = 1
print(f"{a정}")
'''
'''
list = input("").split()
for i in (list):
    print(i)
'''
# print("%8f" % 3.1415) 3.141500
# print("%8.2f" % 3.1415) 3.14
# 숫자 < 알파벳 영문 < 한글  "1" < "a" 문자열 안에서 
# >>> True > False True == 1, False == 0
'''
다른 자료형의 값들을 같은지 비교하면 False, 다른지 확인하면 True를 반환
"abc" == (3 > 2) # 문자열과 불린값 비교
False
"abc" != 3.2 # 문자열과 실수값 비교
True
크기 비교 연산자를 이용해서 다른 자료형을 비교하면 오류 발생
abc" > True
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'str' and 'bool'
'''
'''
if 3:          가능
    print("A")

'''
'''
if score >= 90:        # (1)
    print("A")
elif 80 <= score < 90: # (2)
    print("B")
elif 70 <= score < 80: # (3)
    print("C")
elif score < 70:       # (4)
    print("D")
'''
# pass문 아무것도 하지 않는 명령문
'''
 파이썬의 문자열은 수정할 수 없음
 문자열의 내용을 변경하려 하면 오류 발생
 s = "Hi, everyone.\n"
s[0] = 'h'
TypeError: 'str' object does not support item
'''
# s = "Hello World"
# print(s.index("Wor")) # 6 위치만 알려줌
# print(s.index("wor"))  error 발생
# s.find('o', 0, 4)
# print(s.find("Wor")) # 6 인덱스 값을 반환
# print(s.find("wor")) # -1
# print(s.endswith("a"))
# print("Bye Bye".rfind("Bye"))
# " hello \n".strip() # "hello"만 남음
# lstrip rstrip
# print("가helloh가나".rstrip("가h나")) 가hello
# print("뜨거운 커피".replace("뜨거운", "차가운"))

'''
◼ isalnum()
 문자열이 알파벳과 숫자로만 구성되어 있는지 확인
◼ isalpha()
 문자열이 알파벳만으로 구성되어 있는지 확인
◼ isdigit(), isnumeric()
 문자열의 글자가 숫자로만 구성되어 있는지 확인
◼ islower()
 문자열이 영문 소문자로만 구성되어 있는지 확인
◼ isupper()
 문자열이 영문 대문자로만 구성되어 있는지 확인

◼ upper()
 문자열을 대문자로 변환된 새로운 문자열 반환
◼ lower()
 문자열을 소문자로 변환된 새로운 문자열 반환
◼ swapcase()
 문자열의 대문자는 소문자로 변환, 소문자는 대문자로
변환된 새로운 문자열 반환
◼ count(str)
 문자열에서 주어진 문자열인 str이 몇 번 나오는지 반
환
◼ count(str, start, end)
 문자열에서 주어진 문자열인 str이 몇 번 나오는지 찾
는데 start 부터 end – 1 인덱스내에서만 검색
'''
'''
s=input("")
i = s.rfind('.')
if i != -1:
    print(s[:i])
else:
    print(s[:])
'''
s=input("").strip()
i = s.rfind(".png")
s = s[:i] + ".jpg"
print(s)


