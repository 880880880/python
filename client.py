import json
import yaml
import socket
import zlib
import threading
from datetime import datetime
from argparse import ArgumentParser


def read(sock, buffersize):
    while True:
        response = sock.recv(buffersize)
        if response:
            bytes_response = zlib.decompress(response)
            print(f'\nServer send data {bytes_response.decode()}')
        else:
            pass

def make_request(action, data):
    return {
        'action': action,
        'time': datetime.now().timestamp(),
        'data': data
    }

parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help = 'Sets config file path'
)


args = parser.parse_args()

config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 2048
}

if args.config:
    with open(args.config) as file:
        file_config = yaml.load(file, Loader=yaml.Loader)
        config.update(file_config)

host, port = config.get('host'), config.get('port')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print('Client was started')

    read_thread = threading.Thread(target=read, args=(sock, config.get('buffersize')))
    read_thread.start()

    while True:
        action = input('Enter action: ')
        data = input('Enter data: ')
        request = make_request(action, data)
        str_request = json.dumps(request)
        bytes2send = zlib.compress(str_request.encode())
        sock.send(bytes2send)
        print(f'Client send data {data}')

except KeyboardInterrupt:
    print('client shutdown.')