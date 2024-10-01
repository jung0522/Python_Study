guPopulation = "강남구,233363,강동구,199088,강북구,144410,강서구,267442,관악구,273736,광진구,166638,구로구,180027,금천구,114402,노원구,217272,도봉구,138120"

list = guPopulation.split(",")

print(list)

dic = { }
for i in range(len(list)):
    if i % 2 == 0:
        key = list[i]
    else:
        dic[key] = list[i]
    
print(dic)

num = int(input("인구 수를 입력하시오: "))
found = 0

for key, value in dic.items():
    if num > int(value):
        print(f"{key}:{value}")
        found += 1
    else:
         pass

if (found == 0):
    print(f"인구가 {num}보다 작은 구가 없습니다＂")     

