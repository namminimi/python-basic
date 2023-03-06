#ex04_userText.py
f = open("userText.txt", "w", encoding="utf-8")  #userText 파일 추가 /파일 쓰기
f.close()
while True:
    f = open("userText.txt", "a", encoding = "utf-8") #파일 내용추가 
    userText = input("적고싶은 내용을 작성해 주세요(stop을 누르면 종료합니다.)")
    if userText == 'stop' : break # stop 입력시 종료
    f.write(userText+"\n")
f.close()    
    