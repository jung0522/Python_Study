import sys
file_name=input("파일 이름을 입력하세요: ")
try:
    with open(file_name, "r", encoding="utf-8") as f:
        lines=f.readlines()
        for line in lines:
            print(line.strip())
    
except FileNotFoundError:
    print("찾는 파일이 없습니다.")
    sys.exit()
    


    
   