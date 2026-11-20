import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    
    s.bind(("0.0.0.0", 4433)) # bind do socket TCP
    s.listen(1) # escuta conexões TCP
    print("Server is listening on port 4433...")
    client_socket, address = s.accept() # aceita conexão TCP
    print(f"Received from: {address[0]}")
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        print(data)
        client_socket.send(input("Message: \n").encode("utf-8")) # envia dados para o cliente TCP
        if data == "exit":
            print("Closing connection...")
            client_socket.close() # fecha conexão TCP 
    
except Exception as e:
    print(f"Error: {e}")