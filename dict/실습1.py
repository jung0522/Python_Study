
sentences = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Maecenas porttitor congue massa. 
Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet 
commodo magna eros quis urna. 
Nunc viverra imperdiet enim.
"""

d = {}

lowerSentences = sentences.lower()

# 각 글자들이 딕셔너리에 있는지 확인하고 1을 
# 증가시키거나 1로 초기화
for s in lowerSentences:
    if s in d:
        d[s] += 1
    else:
        d[s] = 1

# key 값 변경하려면 이렇게
d2 = {}
for k, v in d.items():
    if k == ' ':
        k = "SPACE"
    elif k == '\t':
        k = "TAB"
    elif k == '\n':
        k = "NEWLINE"   
    d2[k] = v
    
print(d2)

    