import socket

                          #IPV4              #Protocolo TCP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect(("google.com", 80))
c.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n") # header bruto requisição
p = c.recv(1024).decode("utf-8") # decodifica bytes para string
print(p)