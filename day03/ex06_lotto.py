score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for i in score:
    sum += i

numSum = sum / len(score)
print("평균은 %d"%int(numSum))

##########################################

for x in range(1):
    for z in range(6):
        print("*" * z)
        
        
#######################################
""" import random
num2 = random.randint(0,2)
#print(num2)

user = input("가위바위보중 하나를 입력해주세요: ")

com = ["가위", "바위", "보"]
computer = com[num2]
print("컴퓨터는 %s" %computer)

if user != computer:
    if user == "가위" and computer == "보" or user == "바위" and computer == "가위" or user == "보" and computer == "바위":
        print("이겼습니다")
    else :
        print("졌습니다")       
else :
    print("비겼습니다")  """   

###################################
import random

lottolist = []
userSelect = []
resultlist = []

########### 유저 로또 번호 입력
h = 1
while h <= 6:
    print("1~45 까지 번호를 6개 입력해주세요")
    print("%d번째 번호를 입력해주세요" %h)
    user = int (input())
    if user <= 45:    
        if user not in userSelect:
            userSelect.append(user)
            h += 1
        else :
            print("번호가 중복되었습니다. 다시 입력해주세요")    
            user = input()
    else:
        print("45이하로 입력해주세요")  
              
print("유저 번호 %s" %userSelect)
################ 랜덤 로또번호 
i = 1
while i <= 6:
    num4 = random.randint(1,45)
    if num4 not in lottolist:
        lottolist.append(num4)
        i += 1
    else :
        num4 = random.randint(1,45)    
    
print("랜덤 복권번호 %s" %lottolist)    
################# 유저와 랜덤으로 출력된 번호 비교해줌
count = 0
for u in userSelect:
    for c in lottolist:
        if u == c:
            count += 1
            
print("%d개 맞혔습니다" %count)            