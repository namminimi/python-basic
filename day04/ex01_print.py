#ex01_print.py


print("python" "javascript" "java")
print("python" + "javascript" + "java")
print("python", "javascript", "java")  #한칸씩 띄워쓰기됨 . 문자열 띄워쓰기는 ,임

#print 함수 호출시 end매개변수에 끝문자를 지정할 수 있음
#지정하지 않으면 \n이 지정되어 있음

print(1, end = "") #한줄씩 출력되는 옆으로 출력하고싶으면
print(2)

for i in range(5):
    print(i, end="")