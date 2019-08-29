import yaml
import socket
import logging
import select
import threading
from argparse import ArgumentParser
from handlers import handle_default_request

def read(sock, connections, requests, buffersize):
    try:
        bytes_request = sock.recv(buffersize)
        requests.append(bytes_request)
    except:
        client2kill = str(sock)
        sock.close()
        try:
            connections.remove(sock)
            print(f'Read client with {client2kill} offline')
        except:
            pass


def write(sock, connections, response):
    try:
        sock.send(response)
    except:
        client2kill = str(sock)
        sock.close()
        try:
            connections.remove(sock)
            print(f'Write client {client2kill} offline')
        except:
            pass






parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
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


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('main.log', encoding='UTF-8'),
        logging.StreamHandler()
    ]
)

connections = []
requests = []

host, port = config.get('host'), config.get('port')

try:

    sock = socket.socket()
    sock.bind((host, port))
    sock.setblocking(0)
    sock.settimeout(0)
    sock.listen(5)


    logging.info(f'Server started with { host }:{ port }')

    while True:
        try:
            client, address = sock.accept()
            logging.info(f'Client was detected { address[0] }:{ address[1] }')
            connections.append(client)
            print(connections)
        except:
            pass

        if connections:
            rlist, wlist, xlist = select.select(connections, connections, connections, 0)

            for read_client in rlist:
                read_thread = threading.Thread(
                    target=read, args=(read_client, connections, requests, config.get('buffersize')))
                read_thread.start()
                # try:
                #     bytes_request = read_client.recv(config.get('buffersize'))
                #     requests.append(bytes_request)
                # except:
                #     client2kill = str(read_client)
                #     read_client.close()
                #     connections.remove(read_client)
                #     print(f'Client with {client2kill} offline')

            if requests:
                bytes_request = requests.pop()
                bytes_response = handle_default_request(bytes_request)
                for write_client in wlist:
                    write_thread = threading.Thread(
                        target=write, args=(write_client, connections, bytes_response))
                    write_thread.start()
                    # try:
                    #     write_client.send(bytes_response)
                    # except:
                    #     client2kill = str(write_client)
                    #     write_client.close()
                    #     connections.remove(write_client)
                    #     print(f'Client {client2kill} offline')

        else:
            pass



except KeyboardInterrupt:
    logging.info('Server shutdown.')