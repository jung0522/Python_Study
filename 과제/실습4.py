s = input("파일 이름을 입력하시오: ")

size = len(s)
i = s.rfind(".png")
s = s[:i] + ".jpg"  
print(s)
   
    

