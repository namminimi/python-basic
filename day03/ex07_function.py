#ex07_function.py 함수
#함수 입력값 ---> 함수 ----> 리턴값
# 1.일반적인함수 : 입력값과 리턴값이 있는 함수
def add(a,b):
    print("aaaa")
    return a + b

re = add(10,20)
print(re)
    
#2. 입력값이 없는 함수
def printHi():
    print("안녕")
    return 10

print(printHi())     #리턴값이 없을경우 none 출력됨

#매개변수 지정해서 호출하기
#매개변수를 지정해서 호출하면 순서에 상관없이 사용할수 있음
def sub(a, b):
    return a - b

re2 = sub(a =10, b = 20)
print(re2)

# 입력값이 몇개가 될 지 모를때 *매개변수 
# 입력값을 전부 모아서 튜플로 만들어줌!!!!
def addMany(*args):
    result = 0
    for i in args:
        result = result + i
    return result
re3 = addMany(1, 2, 3, 4, 5)
re4 = addMany(2, 3, 4)    

print(re3)
print(re4)

#매개변수에 초기값 설정하기
def sayMy(name, age , man=True):
    print("나의 이름은 %s 입니다"%name)
    print("나의 나이는 %d살 입니다" %age)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")
            
sayMy("김그린", 22)
sayMy("이블루", 30, False)  



#######복습
#12345를 인수로 받아서 [5,4,3,2,1]리턴
# int("100") ====> 정수로 형변환
# list() ====> 리스트로 형변환
# str() ====> 문자로 형변환
def solution(n):
    answer = []
    for i in str(n):
        answer.append(int(i))
    answer.reverse()
    return answer
print(solution(12345))


def avgNumber(*nums):
    result= 0
    for i in nums:
        result += i
        result2 = result / len(nums)
    return result2
    
print(avgNumber(1,2,3))
print(avgNumber(5,6,8,9,8))    

#람다 함수
#lambda 매개변수1, 매개변수2 : 매개변수를 사용한 표현식
lambdaAdd = lambda a, b : a + b

    