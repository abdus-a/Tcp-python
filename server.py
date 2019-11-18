import socket
import random
#Creating the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
prime_numburs = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
randome_for_p = random.radint(0,24)
randome_for_g= random.radint(0,24)
g = prime_numburs[randome_for_g]
p = prime_numburs[randome_for_p
def diffeihelmen_keyPublicMake_for_a(p, g):
    a = random.randint(1,96)
    A = g**a%p
    
host = socket.gethostname() #Host is the server IP
port = 444 #Port to listen on 
#Binding to socket
serversocket.bind((host, port)) #Host will be replaced/substitued with IP, if changed and not running on host

#Starting TCP listener
serversocket.listen(3)

while True:
    #Starting the connection 
    clientsocket,address = serversocket.accept()

    print("received connection from " % str(address))
    
    #Message sent to client after successful connection
    #message = 'hello! Thank you for connecting to the server' + "\r\n"
    
    #clientsocket.send(message)
    
#    clientsocket.close()
