s = "Hello World"
s.index("Wor") # 6
# s.index("wor") # error 발생
print()

s.find("Wor") # 6 
s.find("wor") # -1
print()

str1 = "가helloh가나"
print(str1.strip("가h나")) # "ello"만 남음, 저장해줘야 함
print(str1)
print("가helloh가나".lstrip("가h나"))

print()
print("뜨거운 커피".replace("뜨거운", "차가운"))
print()

ex_string = "2312321dsajfaji3ednwasjo"
print(ex_string.count("j"))
print(ex_string.upper())
print(ex_string.lower())
print(ex_string.isdigit())
print(ex_string.isalpha())
print(ex_string.isalnum())
print("i".islower())
print("i".isupper())
