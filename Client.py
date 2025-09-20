import socket

HOST='127.0.0.1'
PORT=1234

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))
print ("Connected to Server....!")

while True:
    msg = input(f"Client : ")
    client.send(msg.encode())
    if not msg or msg.lower()=='bye':
        print("Server connection closed....!")
        break
    
    reply =  client.recv(1024).decode()
    print(f"Server : {reply}")
    if not reply or reply.lower()=='bye':
        print("Server connection closed....!")
        break
client.close()