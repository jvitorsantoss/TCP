import socket

                          #IPV4              #Protocol TCP
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
c.connect(("google.com", 80))
c.send(b"Ola, mundo")
c.recv(1024)