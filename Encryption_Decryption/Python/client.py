import socket
import random
def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr(ord(char) + s) 

        else:
            result += chr(ord(char) + s)
    return result


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)      

udp_host = socket.gethostname()		
udp_port = 12345			        
shift=random.randint(0,10)
msg = input("Enter the message:")
print("UDP target IP:", udp_host)
print("UDP target Port:", udp_port)
x=encrypt(msg,shift)
sock.sendto(x.encode('ascii'),(udp_host,udp_port))
sock.sendto(str(shift).encode('ascii'),(udp_host,udp_port))
