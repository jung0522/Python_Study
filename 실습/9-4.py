filename = input("파일 이름을 입력하세요: ")

try:
    with open(filename, encoding = "utf-8") as f:
        c = f.read()
        print(c.strip())
except UnicodeDecodeError:
    with open(filename, encoding = "cp949") as f:
        c = f.read()
        print(c.strip())