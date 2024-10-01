ta, tw = map(float, input("건구 온도와 습구 온도를 입력하시오: ").split())

DiscomfortIndex = 0.72 * (ta + tw) + 40.6

if ( 0 <= DiscomfortIndex < 68 ):
    print(f"불쾌지수는 {DiscomfortIndex:.2f}이고, 모든 사람이 쾌적함을 느낌" )

elif ( 68 <= DiscomfortIndex and DiscomfortIndex < 75 ):
    print(f"불쾌지수는 {DiscomfortIndex:.2f}이고, 불쾌감을 나타내기 시작함" )

elif ( 75 <= DiscomfortIndex and DiscomfortIndex < 80 ):
    print(f"불쾌지수는 {DiscomfortIndex:.2f}이고, 반 정도의 사람이 불쾌감을 느낌" )

elif ( 80 <= DiscomfortIndex and DiscomfortIndex <= 100 ):
    print(f"불쾌지수는 {DiscomfortIndex:.2f}이고, 모든 사람이 불쾌감을 느낌" )

else:
    print(f"불쾌지수는 0 ~ 100입니다" )

