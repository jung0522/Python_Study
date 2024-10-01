weight = int(input("무게를 입력하시오: "))

if ( 0 < weight and weight <= 5):
    print("우편 요금은 %d입니다." % 400)

elif (5 < weight and weight <= 25):
    print("우편 요금은 %d입니다." % 430)

elif ( 25 < weight and weight <= 50):
    print("우편 요금은 %d입니다." % 450)

elif ( 50 < weight):
    print("우체국에 문의하십시오")

else:
    print("적절하지 않은 무게입니다.")
