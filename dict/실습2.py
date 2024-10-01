guPopulation = "강남구,233363,강동구,199088,강북구,144410,강서구,267442,관악구,273736,광진구,166638,구로구,180027,금천구,114402,노원구,217272,도봉구,138120"

list1 = guPopulation.split(",")


dic = { }

for i in range(len(list1)):
    if i % 2 == 0:
       dic[list1[i]] = int(list1[i+1])
    else:
        continue
    
n = int(input("인구 수를 입력하시오: "))

found = 0

for k, v in dic.items():
    if n > v:
        print(f"{k}:{v}")
        found += 1

if found == 0:
    print(f"{n}보다 작은 인구수의 도시가 없습니다.")
    
   