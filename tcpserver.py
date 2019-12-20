import socket

s=socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
s.bind(('',1000))
s.listen(5)
print("socket is listening")
while True:
    c,addr=s.accept()
    print("got connection from",addr)
    c.send(b'hello')
    p=c.recv(1024)
    print("client says=",p.decode())
    s2=str.encode("")
    while s2.decode()!="bye":
        s1=input("server:=")
        c.send(str.encode(s1))
        s2=c.recv(1024)
        print("client=",s2.decode())
    c.close()
