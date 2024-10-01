
a=[1,2,3,4,5,6,7,8,9,10]
name=["인도","중국","미국","인도네시아","파키스탄"]

name_length = 0
for i in range(5):
    name_len=(len(name[i]))
    padding =(10- name_len)
    print(f'{i+1:^3}위 나라는 %-{padding}s입니다'%name[i])
    
