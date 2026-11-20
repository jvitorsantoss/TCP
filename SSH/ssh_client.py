import paramiko
import subprocess


host = input('Enter host: ')
user = input('Enter username: ')
passwd = input('Enter password: ')

c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Conecta em conexões SSH sem verificar a chave do host
c.connect(host, username=user, password=passwd) #Passa os parâmetros para a conexão SSH
stdin, stdout, stderr =c.exec_command("ls") #Execução do comando ls no host remoto
