linNum = 1
found = False
filename = input("파일 이름을 입력하세요: ")
findStr = input("검색할 문자열을 입력하세요: ")

with open(filename, encoding="utf-8") as f:
    for line in f.readlines():
        if findStr in line:
            found = True
            print("%d:%s" % (linNum, line.strip()))
        linNum += 1
        
if found == False:
    print("찾는 문자열이 없습니다")

