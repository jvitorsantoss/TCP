import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    while True:
        s.bind(("0.0.0.0", 4433)) # bind do socket TCP
        s.listen(1) # escuta conexões TCP
        print("Server is listening on port 4433...")
        client_socket, address = s.accept() # aceita conexão TCP
        print(f"Received from: {address}")
        s.close() # fecha socket TCP
except Exception as e:
    print(f"Error: {e}")