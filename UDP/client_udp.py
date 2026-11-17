import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # IPV4, Protocolo UDP
try:
    while True:
        msg = input("Menssage: ") + "\n" # recebe mensagem do usuário
        c.sendto(msg.encode(), ("localhost", 12345)) # envia dados para o servidor UDP
        data, sender = c.receivefrom(1024) # recebe dados do servidor UDP
        print(sender[0] + ": " + data.decode())
except Exception as e:
        print(f"Error: {e}")    