print ("한병준의 서버 구동기에 오신것을 환영합니다")
print("서버의 메모리 용량을 정해주세요 (보통1~2")
server_memorysize = input(" ")
print("서버 파일의 이름을 입력해주세요. (.jar 포함)")
server_name = input(" ")
server_start_file = open("server_start.bat","w")
server_start_file.write("java -Xms" + (server_memorysize) + "G -Xmx" + (server_memorysize) + "G -jar " + (server_name) + 
' pause')
eula = open("eula.txt","w")
eula.write("eula=true")
