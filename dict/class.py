'''
변경 불가능한 것들만 사용할 수 있음
문자열, 숫자, 불린 값, 튜플 등
리스트 안 됨
'''

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
print(d[1])
print(d[False])
print(d[(1,2)])
print()

d = { "name" : "홍길동", "age" : 20, 
  "취미" : ["영화 감상", "게임", "독서"] }
print(d["name"]) # 홍길동
print(d["취미"]) # ["영화 감상", "게임", "독서"]
# print(d["이름"]) # 오류 발생 (KeyError)
print()

d = { "name" : "홍길동", "age" : 20, 
  "취미" : ["영화 감상", "게임", "독서"] }
print(d.get("name")) # 홍길동
print(d.get("취미")) # ["영화 감상", "게임", "독서"]
print(d.get("이름")) # None 오류가 아니라 없다고 나옴
print()

d = { 1 : 2, True : 20, (1, 2) : "튜플" }
print(d[1])
print(d[True])
print(d[(1,2)])
print()

d = { "name" : "홍길동", "age" : 20,  "취미" : ["영화 감상", "게임", "독서"], "name" : "김길동" }
print(d["name"]) # 김길동 나중에 나오는 값
print(d["취미"]) # ["영화 감상", "게임", "독서"]
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d[1] = 3
d[False] = "불린 값"
d[(1, 2)] = [1, 2]
d["key"] = "value"   # 새로운 키와 값 추가
print(d[1])
print(d[False])
print(d[(1,2)])
print(d["key"])
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d.update({1:3, False:"불린 값", (1,2):[1,2], "key":"value" })
print(d[1])
print(d[False])
print(d[(1,2)])
print(d["key"])
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for key in d:
    print(f"{key}:{d[key]}")

print()
   
d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for key in d.keys():
    print(f"{key}:{d[key]}")
    
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for n in d.values():
    print(n)

print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
for k, v in d.items():
    print(k, v)

print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
if 1 in d:
    print(1, d[1])
else:
    print("1은 d의 키가 아닙니다")
    
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
del(d[1])
print(d) # { False : 20, (1, 2) : "튜플" }
print()

d = { 1 : 2, False : 20, (1, 2) : "튜플" }
d.clear()
print(d) # {}
print()

# 주의할 점 키 값으로 리스트 사용 불가





