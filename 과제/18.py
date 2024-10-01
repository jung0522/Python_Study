year, month, day = map( int, input("년/월/일을 입력하시오: ").split('/'))

if ( 1 <= month and month <= 12 ):  
    if (month == 2):
        
        if (1 <= day and day <= 28):
           print(f"{year}년 {month}월 {day}일")

        else:
           print("적절한 날짜가 아닙니다.")

    elif ( month <= 7):
        
        if( month % 2 != 0):
            
           if (1 <= day and day <= 31):
              print(f"{year}년 {month}월 {day}일")

           else:
              print("적절한 날짜가 아닙니다.")

        else:
        
           if (1 <= day and day <= 30):
              print(f"{year}년 {month}월 {day}일")

           else:
              print("적절한 날짜가 아닙니다.")
    else: 
        if( month % 2 != 0):
            
           if (1 <= day and day <= 30):
              print(f"{year}년 {month}월 {day}일")

           else:
              print("적절한 날짜가 아닙니다.")

        else:
        
           if (1 <= day and day <= 31):
              print(f"{year}년 {month}월 {day}일")

           else:
              print("적절한 날짜가 아닙니다.")
else:
    print("적절한 날짜가 아닙니다.")
    
