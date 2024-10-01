while (1):
        filename = input("파일 이름 입력: ")
        try:
            f = open(filename, encoding = "utf-8")
            s = f.read()
            print("utf-8")
        except UnicodeDecodeError:
            f = open(filename, encoding = "cp949")
            s = f.read()
            print("cp949")
        f.close() 
        # s에는 파일의 내용이 있음
        print(s)
