import socket
import random
def decrypt(text,sr):
    s=int(sr)
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr(ord(char) - s) 
        else:
            result += chr(ord(char) - s) 
    return result
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
sock.bind((udp_host,udp_port))
print("Waiting for client...")
data,addr = sock.recvfrom(1024)	        
print("Given Encrypted Message:",data," from",addr)
print("Waiting for client...")
shift,addr = sock.recvfrom(1024)	        
x=decrypt(data.decode('ascii'),shift.decode('ascii'))
print("Message after decryption:",x)
shift_k=random.randint(0,10)
p=encrypt(x,shift_k)
print("Message after encryption:",p)
f = open("file.txt", "a")
f.write(p+"\n")
f.write(str(shift_k)+"\n")
f.close()

