import time
import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
u_host=socket.gethostname()
u_port=8529
msg=b'hello'
print("udp ip",u_host)
print("udp port",u_port)
sock.sendto(msg,(u_host,u_port))
time.sleep(20)
print("end")
