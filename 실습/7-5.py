import math 
T1 = ("사각형", 30, 20, "원", 10, "원", 20, "사각형", 60, 40)

def calcAndPrintArea(T1):
    for i in range(len(T1)):
            if T1[i] == "사각형":
               print(f"도형 종류: {T1[i]},", end=" ")
               print("%d x %d = %d " % (T1[i+1], T1[i+2], T1[i+1] * T1[i+2] ))
            elif T1[i] == "원":
               print(f"도형 종류: {T1[i]},", end=" ")
               print("%d x %d x 3.14 = %.2f " % (T1[i+1], T1[i+1], T1[i+1] **2 * math.pi))

calcAndPrintArea(T1)
                
            
