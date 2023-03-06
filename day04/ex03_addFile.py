#ex03_addFile.py
#내용 추가
f = open("test.txt", "a", encoding="utf-8") #encoding="utf-8"이 없으면 글자 깨짐
for i in range(5,9): 
    data = "%d 번째 줄입니다.\n" %i
    f.write(data)
f.close()    