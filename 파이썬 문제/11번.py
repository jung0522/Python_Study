filename=input("파일 이름을 입력하세요: ")

try:
    f= open(filename)
    lines=f.readlines()
    
except:
    print("cp949 방식으로 읽는 데 실패했습니다. utf-8 방식으로 읽어봅시다.")
    f= open(filename, encoding="utf-8")
    lines=f.readlines()
    print(lines)

f.close()

    
   