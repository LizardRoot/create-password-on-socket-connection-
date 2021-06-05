import os 
import socket
import re
import subprocess
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '127.0.0.1'
port = 3333

s.bind((host, port))
s.listen(1)
print('')
print('wait for connection...')
print('')
conn, addr = s.accept()

def shell():
	while True:
		command = input(str('#> '))

		if command == 'system':
			conn.send(command.encode())

			sysinfo = conn.recv(10000)		
			sysinfo = sysinfo.decode()

			print('')
			for i in sysinfo.split(','):
				i = re.sub(r"[,() ']", "", i)
				print(i)
			print('')

def auth():
	pwd = conn.recv(1024)
	pwd = pwd.decode()
	print(pwd)

	password = input(str(''))
	conn.send(password.encode())

	check = conn.recv(1024)
	check = check.decode()

	if check == 'ok':
		shell()
	else:
		auth()

auth()
