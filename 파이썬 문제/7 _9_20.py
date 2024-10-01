# 7
my = [1, 2]
my.append([3,4])
print(my)

# 19
for i in my:
    print(i, end =" ")
    
# 20
print("")
value = 6
if value in my:
    i = my.index(value)
    print(f"my의 {i} index에 {value}가 있습니다.")
else:
    print(f"{value}가 my에 없습니다.")
