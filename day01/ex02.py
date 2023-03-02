num1 = 10
num2 = 3


#연산자
#+:덧셈, -:뺄셈, *:곱셈, /:나눗셈, **:제곱근, %:나머지, //:몫(정수)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 + num2)
print(num1 - num2)

#문자열 곱하기 *
print("=" * 20)

#문자열 더하기 +
head = "Python"
tail = "is funs"
print(head+tail)
print(head*2)
#문자열 길이구하기 1en(변수)
a = "python"
print(len(a))

#문자열 인덱싱
print(a[5])
#문자열 슬라이싱 문자열[시작번호: 끝번호] - 끝번호 제외
print(a[0:2])
print(a[:3])
print(a[2:])

#문자열 포매팅 : 문자열안에 어떤 값을 넣기
#문자열 포맷코드
#%d 정수 %s 문자열 %f 소수
num = 3
str3 = "어제"
print("나는 %s 사과 %d개를 먹었다" % (str3, num))

#소수점 표현하기
print("%0.4f" %3.123456789)

#format함수 사용하기
num2 = 10
print("나는 {0} 사과 {1}개를 넣었다" .format("어제",num))

print("나는 {0} 사과 {num2}개를 넣었다" .format(str3,num2=30))
number3 = 20
print("현재 온도는 {0}입니다. 내일 온도는 {to}입니다 " .format(number3, to=3))

#f.포메팅
name = "green"
age = 30
print(f'나의 이름은 {name}이고 나이는 {age}이다')
print(f'내년이면 내 나이는 {age+1}이됩니다')