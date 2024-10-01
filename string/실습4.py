str1 = input("입력하시오: ")

if (str1.rfind(".jpg") != -1):
    # str1 = str1[:str1.rfind(".jpg")] + ".png"
    str1 = str1.replace(".jpg", ".png") # 저장 중요
    print(str1)
    
else:
    print(str1)