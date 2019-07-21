import socket, json
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-a', '--addr', type=str, required=False, help='Sets host address') 
parser.add_argument('-p', '--port', type=str, required=False, help='Sets port')

args = parser.parse_args()

config = {'addr': 'localhost', 'port': 7777, 'buffersize': 1024}

if args.addr: config['addr'] = args.addr
if args.port: config['port'] = args.port

host, port = config.get('addr'), config.get('port')

presencemessage = {
    'action': 'authenticate',
    'time': 'time',
    'user': {'account_name': 'User0', 'password': 'password'}
}

try:
    clientsocket = socket.create_connection((host, port))
    clientsocket.send(json.dumps(presencemessage).encode())
    print(f'Client send presence: {presencemessage}')
    recvdata = json.loads(clientsocket.recv(config['buffersize']).decode())['responce']
    if recvdata == 200:
        print('Server sends OK')
    else:
        print('Something goes wrong')
except KeyboardInterrupt:
    print('client shutdown.')
