while True:
    try:
        file_name=input("파일 이름을 입력하세요: ")
        file = open(file_name, "r", encoding="utf8")
        line=file.read()
        print(line)
        file.close()
        break
    except:
        print("파일을 찾을 수 없습니다. 다시 입력하세요.")