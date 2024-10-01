# 파이썬 코드를 이용해서 현재 작업 디렉토리를 찾는 방법
import os
print(os.getcwd())

'''
t.txt에 쓰기
f = open("t.txt", "w")
f.write("hello world\n")
f.write("hello world")
f.close()
'''
'''
f = open("t.txt") # 열기, f = open("t.txt", "r")
s = f.read() # 파일 내용 전체 읽기
print(s) # 읽은 내용 출력
f.close() # 파일 닫기
'''

f = open("t.txt") # f = open("./t.txt", 'r') 파일 전체를 읽어서 리스트에 저장
# 파일 전체의 내용을 리스트로 만듦
lines = f.readlines() # readlines()는 리스트 readline은 str
for line in lines:
 print(line.strip())
f.close() # 파일 닫기


'''
with open("t.txt") as f: # with는 두 개의 연산 동시 실행 ex> open - close
    for line in f.readlines():   # == for line in f.readlines(): 리스트 형태로 읽기 때문에
        print(line.strip()) # line은 '\n'이 포함되어 있기 때문에 strip을 통해 써주기
'''
'''
f = open("t.txt") # f = open("t.txt", "r")
line = f.readline() # 한 줄 읽어옴
while line: # 파일의 끝에 도달하면 False
    print(line, end = '')
    line = f.readline()
f.close() # 파일 닫기
'''
'''

os.chdir("./python_file")
print(os.getcwd())
with open("./txtxtx.txt", "w+", encoding="utf-8") as f:
    content = "정준영"
    f.write(content)
with open("../txtxtx.txt", "w+", encoding="utf-8") as f:
    content = "정준영"
    f.write(content)
'''

'''
with open("t.txt") as f:
    s1 = f.read()
    
with open("t2.txt", "w+", encoding="utf-8") as f2:
    f2.write(s1)
    
with open("t2.txt", encoding="utf-8") as f2:
    s2 = f2.read()
    print(s2.strip())
'''

'''
f_1 = input("f1을 입력하시오: ")
f_2 = input("f2를 입력하시오: ")
nf = input("nf를 입력하시오: ")

with open(f_1) as f1:
    s1 = f1.read()

with open(f_2) as f2:
    s2 = f2.read()
    
f3 = open(nf, "w+", encoding="utf-8") 
f3.write(s1)
f3.write("\n")
f3.write(s2)     
f3.close()

f3 = open(nf, "r+", encoding="utf-8") 
content = f3.read()
print(content)
'''


import sys
sys.exit()