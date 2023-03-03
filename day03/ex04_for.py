#ex04_for.py

list1 = ["one", "two", "three"]
for i in list1:
    print(i)
    
for i in "green":
    print(i)
    
marks = [90, 50, 67, 70, 80]
number = 0
for stu in marks:
    number = number + 1
    if stu >= 70:
        print("%d번 학생은 합격입니다" %number)
    else:
        print("%d번 학생은불합격입니다" %number)            
##########################################################        
print(list(range(2,10,2)))        

#range()함수 range(stop), range(start, stop), range(start, stop, step)
sum = 0
for i in range(1,11,2):
    sum = sum + i
print('1~10까지 더한수는 %d이다'%sum)    

#for 와 range를 사용해서 구구단 출력
for i in range(1,10):
    print("{0}단".format(i))
    for z in range(1,10):
        print("{0} * {1} = {2}" .format(i,z, i*z))
        
        #print('%d * %d = %d'%(i,z,i*z))