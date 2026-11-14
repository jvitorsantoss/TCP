import socket

                          #IPV4              #Protocolo TCP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect(("google.com", 80))
c.send(b"GET / HTTP/3\nHost: www.google.com\n\n\n") # header bruto requisição
c.recv(1024)