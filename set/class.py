'''
집합(set) 자료구조
수학에서의 집합을 나타내는 자료구조
 순서가 없고, 동일한 데이터가 두 개 이상 존재할 수 없음
집합 관련 연산(교집합, 합집합, 차집합) 지원
중괄호로 표시

특정 요소에 접근 불가
집합에는 리스트는 포함 못함(튜플은 가능)
집합을 리스트로 변환

집합의 요소 개수 확인

'''

s = set()
print(s)
s = set([1, 2, 3])
print(s)
s = set("abc")
print(s)
s = set("yellow")
print(s)

a = set([1, 2, 3])
a.add("abc")
print(a)

a = set([1, 2, 3])
a.update("string")
print(a)

print()
s1 = { 1, 2, 20, (1, 2), "문자열" }
s2 = { 1, 2, 3 }
ints = s1 & s2 # ints = s1.intersection(s2)
print(ints)

unions = s1 | s2
unions = s1.union(s2)
print(unions)

diffs = s1.difference(s2)
print(diffs)

s = { 1, 2, 20, (1, 2), "문자열" }
if 1 in s:
    print("1은 집합 s에 포함되어 있습니다")
else:
    print("1은 집합 s의 요소가 아닙니다")
