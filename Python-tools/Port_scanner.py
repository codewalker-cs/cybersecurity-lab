import socket
import threading

order_ports = []
lock=threading.Lock()

def scan_ports(ip,port):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result=s.connect_ex((ip,port))
    if (result==0):
        with lock:
            order_ports.append(port)
    s.close()

d=input("Enter the domain who's port you want to scan:")
ip=socket.gethostbyname(d)
print("="*50)
print(f"Target: {d}")
print(f"IP: {ip}")
print(f"Ports: 1-1024")
print("="*50)

threads=[]
for port in range(1,1025):
    t=threading.Thread(target=scan_ports,args=(ip,port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

for i in sorted(order_ports):
    print(f"[OPEN] Port {i}")

print("Scan is Complete!")