while True:
    try:
        s=input("정수를 입력하세요: ")
        n = int(s)
        break
    except:
        print("숫자가 입력되지 않았습니다")