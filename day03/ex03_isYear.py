""" *년도를 입력받아서 윤년인지 평년인지 나타내주세요
1. 연수가 4로 나누어 떨어지는 해는 윤년으로한다
2. 이중에서 100으로 나누어 떨어지는 해는 평년으로 한다
3. 그중에 400으로 나누어 떨어지는 해는 윤년으로 한다.
-정수로 년도를 받습니다
-입력받은 년도가 윤년인지 평년인지 출력하세요 """

year = int (input("년도를 입력해주세요: "))
if year % 4 == 0:
    if year % 100 == 0:
        yearText = "평년" 
        yearText = "윤년" if year % 400 == 0 else "평년"
    else :
        yearText = "윤년"
else :
    yearText = "평년"            
print(yearText)    