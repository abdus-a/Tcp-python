import socket

#Create socket object
clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#host = '192.168.1.104'
host = socket.gethostname()

port = 444
def diffeihelmen_keyPublicMake_for_b(p,g):
    b = random.randint(1,95)
    B = g**b%p
    return B

clientsocket.connect(('192.168.1.104', port)) #You can substitue the host with the server IP

#Receiving a maximum of 1024 bytes
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
