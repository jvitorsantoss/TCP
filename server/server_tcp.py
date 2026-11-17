import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind(("0.0.0.0", 4433)) # bind do socket TCP
    s.listen(1) # escuta conexões TCP
    print("Server is listening on port 4433...")
    s.accept() # aceita conexão TCP
except Exception as e:
    print(f"Error: {e}")