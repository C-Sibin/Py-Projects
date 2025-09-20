import socket
import threading

Bind_IP = '0.0.0.0'
Bind_PORT = 1234

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((Bind_IP,Bind_PORT))

server.listen(5)

print ("Server listening on : %s-%d"%(Bind_IP,Bind_PORT))

client,addr = server.accept()

'''def client_handler(client,addr):
    msg = client.recv(1024)
    if msg or msg.lower() == 'bye':
        print("Connection closed....")
        server.close()
        client.close()

    reply = input(f"Server : ")
    client.send(reply.encode())
    if reply or reply.lower == 'bye':
        print("Connection closed....")
        server.close()
        client.close()

    server.close()
    client.close()

while True:
    client,addr = server.accept()
    print(f"Server accepted some data....From : {addr}")
    client_data = threading.Thread(target=client_handler,args=(client,addr))
    client_data.start() '''

while True:
    msg = client.recv(1024).decode()
    print(f"Client : {msg}")
    if not msg or msg.lower() == 'bye':
        print("Client connection closed....")
        break

    reply = input(f"Server : ")
    client.send(reply.encode())
    if not reply or reply.lower == 'bye':
        print("Connection closed....")
        break

server.close()