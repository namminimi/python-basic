#ex02_file.py
#파일 생성
f = open("test.txt", "w", encoding="utf-8")

""" f.write("하하하하하하하하")
f.close() """
students = ["이나영", "김아랑", "강하늘", "김우리"]
scores = [98,80,77,65]
#파일 쓰기
for i in range(4):
    data = "%s님은 %s 점입니다. \n" %(students[i], scores[i])
    f.write(data)
f.close()   

#파일 읽기
d = open('test.txt', 'r', encoding = 'utf-8')
""" readData = d.readlines() #모든줄을 리스트 반환
for i in readData:
    print(i)  """
""" readData = d.readline() # 첫번째 줄만 반환
print(readData)  """

readData = d.read() # 모든 줄을 문자열로 반환
print(readData)   
    
d.close()    