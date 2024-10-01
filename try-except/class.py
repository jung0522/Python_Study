'''
print("오류 발생 확인 프로그램")
n = int(input("정수를 입력하세요: ")
print(f"사용자가 입력한 정수: {n}")
[실행 결과]
File "SyntaxError.py", line 2
 n = int(input("정수를 입력하세요: ")
        ^
SyntaxError: '(' was never closed
'''
'''
>>> n = int(input("정수를 입력하세요: "))
정수를 입력하세요: 23.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '23.5'
'''
'''
실행 오류가 발생하는 몇 가지 예
int() 명령에 실수 형태로 된 문자열을 전달
문자열에서 index() 함수를 사용하는데 찾는 문자열 없음
open() 함수를 이용해서 파일을 열 때 파일이 없는 경우
리스트에 있는 요소 개수보다 큰 범위의 요소를 접근
0으로 나누는 경우
'''
'''
print("예외 처리 확인 프로그램")
try:
    s = input("정수를 입력하세요: ")
    n = int(s)                                     # (1)
    print(f"사용자가 입력한 정수: {n}")             # (2)
except:
    print(f"정수로 변환할 수 없습니다. 입력값: {s}") # (3)
print("프로그램 종료")                              # (4)
'''
'''
lst = [1, 2, 3]
idx = int(input("변경할 요소의 위치(인덱스)를 입력하세요: "))
n = int(input("새로운 값을 입력하세요: "))     # (1)
lst[idx] = n # idx 위치의 요소 값을 n으로 변경 # (2)
print(lst)
'''

'''
try:
    lst = [1, 2, 3]
    idx = int(input("변경할 요소의 위치(인덱스)를 입력하세요: "))
    n = int(input("새로운 값을 입력하세요: "))
    lst[idx] = n # idx 위치의 요소 값을 n으로 변경
    print(lst)
except: # 모든 오류를 한 곳에서 대응
    print("오류: 인덱스 범위를 벗어났거나 정수가 아닌 문자열을 입력했음")


try:
    lst = [1, 2, 3]
    idx = int(input("변경할 요소의 위치(인덱스)를 입력하세요: "))
    n = int(input("새로운 값을 입력하세요: "))
    lst[idx] = n # idx 위치의 요소 값을 n으로 변경
    print(lst)
except ValueError: # ValueError에 대응
    print("오류: 정수가 아닌 문자열을 입력했음")
except IndexError: # IndexError에 대응
    print("오류: 인덱스 범위를 벗어남")

try:
    lst = [1, 2, 3]
    idx = int(input("변경할 요소의 위치(인덱스)를 입력하세요: "))
    n = int(input("새로운 값을 입력하세요: "))
    lst[idx] = n # idx 위치의 요소 값을 n으로 변경
    print(lst)
except ValueError: # ValueError에 대응
    print("오류: 정수가 아닌 문자열을 입력했음")

try:
    lst = [1, 2, 3]
    idx = int(input("변경할 요소의 위치(인덱스)를 입력하세요: "))
    n = int(input("새로운 값을 입력하세요: "))
    lst[idx] = n # idx 위치의 요소 값을 n으로 변경
    print(lst)
except ValueError: # ValueError에 대응
    print("오류: 정수가 아닌 문자열을 입력했음")
except: # 나머지 (IndexError, NameError)에 대응
    print("오류 발생")
     
'''

'''

import sys
try:
    fname = "c:\\temp\\a.ini"
    f = open(fname)
    lines = f.readlines()
    f.close()
except FileNotFoundError: # FileNotFoundError 발생
    print("Could not open " + fname)
    sys.exit()
except:   # 다른 오류 일괄 처리
    print("Other error occurred")
print("End of the program")
'''

try:
    print(3 / 0)   # 오류 발생
except ZeroDivisionError:
    pass           # 예외 처리로 아무것도 안함
print("오류가 발생함에도 여기까지 출력됨")
