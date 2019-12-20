import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
u_host=socket.gethostname()
u_port=8529
print("udp ip",u_host)
print("udp port",u_port)
sock.bind((u_host,u_port))
while True:
    print("waiting for client")
    data,addr=sock.recvfrom(1024)
    print("received msg:",data,"from",addr)
