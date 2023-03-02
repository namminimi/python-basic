#이모지 사용하면 터미널에서 깨짐현상 발생 터미널에서는 안보이는듯
list1 = ["a","b","c","d"]
print(list1)
print(type(list1))
print(list1[1])
#리스트의 슬라이싱 --- 슬라이싱은 나는다는 뜻
print(list1[2:])
list2 = [1, 2, 3]
list3 = [4, 5, 6]
#리스트 더하기 +기호를 사용하면 리스트를 합쳐준다
list4 = list2 + list3
print(list4)
#리스트 반복하기 *기호를 사용하면 리스트를 반복해서
#새로운 리스트를 반환함
list5 = list2 * 3
print(list5)
#리스트 길이 구하기 len(리스트)
print(len(list5))
#리스트 수정, 삭제(del 객체) -모든 자료형 삭제 가능
list2[0] = 10
print(list2)
del list2[0]
del list5[4:]
print(list5)
print(list2)

students = ["stu1","stu2","stu3","stu4"]
#리스트에 요소추가 append(value)
students.append("stu5")
print(students)
#리스트에 요소추가 (원하는 위치에) insert(start,value)
students.insert(1,"newStu")
print(students)
#리스트 뒤집기 reverse()
students.reverse()
print(students)
#리스트 정렬 sort()
students.sort()
print(students)
numberList = [5,2,1,6,7,8,2,10]
numberList.sort()
print(numberList)
#인덱스반환 index(value) , 없는 인덱스 출력시 오류 발생
num = students.index("stu3")
print(num)
#리스 요소 제거 remove(value)
students.remove("stu3")
print(students)
numberList.remove(2)
print(numberList)
#리스트 마지막요소 리턴후 삭제 pop()
lastList = students.pop()
print(lastList)
print(students)
#리스트에 포함된 요소의 개수 세기 count(value)
fruits = ["사과", "딸기", "사과", "바나나", "사과", "귤"]
applenum = fruits. count('사과')
print(applenum)
