import socket
s=socket.socket()
s.connect(('127.0.0.1',1000))
s1=s.recv(1024)

print("server:",str(s1,"utf-8"))
s.send(b'hi')
s2=""
while s2!="bye":
    s1=s.recv(1024)
    print("server:=",s1.decode())
    s2=input("client:=")
    s.send(str.encode(s2))
print("party Close......")
s.close()
