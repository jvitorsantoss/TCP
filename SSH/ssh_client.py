import paramiko

host = '127.0.0.1'
user = 'kali'
passwd = 'kali'

c = paramiko.SSHClient()
c.connect(host, username=user, password=passwd)