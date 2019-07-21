import json, socket
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('-a', '--addr', type=str, required=False, help='Sets host address')
parser.add_argument('-p', '--port', type=str, required=False, help='Sets port')

args = parser.parse_args()

config = {'addr': '', 'port': 7777, 'buffersize': 1024}

if args.addr: config['addr'] = args.addr
if args.port: config['port'] = args.port

host, port = config.get('addr'), config.get('port')

try:
    servsocket = socket.socket()
    servsocket.bind((host, port))
    servsocket.listen(5)
    print('Server started')
    while True:
        client, address = servsocket.accept()
        print(f'Connection accepted from: {address[0]}:{address[1]}')
        b_req = client.recv(config.get('buffersize'))
        if json.loads(b_req)['action']=='authenticate': client.send(json.dumps({'responce':200}).encode())
        print(f'Client sends message: {b_req.decode()}')
        client.close()
except KeyboardInterrupt:
    print('client shutdown.')
