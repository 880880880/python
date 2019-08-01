import json
import yaml
import socket
import logging
from argparse import ArgumentParser
from protocol import validate_request, make_response
from actions import resolve



parser = ArgumentParser()

parser.add_argument(
    '-c', '--config', type=str, required=False,
    help='Sets config file path'
)

args = parser.parse_args()

config = {
    'host': 'localhost',
    'port': 8000,
    'buffersize': 1024
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

host, port = config.get('host'), config.get('port')

try:

    sock = socket.socket()
    sock.bind((host, port))
    sock.listen(5)

    logging.info(f'Server started with { host }:{ port }')

    while True:

        client, address = sock.accept()
        logging.info(f'Client was detected { address[0] }:{ address[1] }')

        b_request = client.recv(config.get('buffersize'))
        request = json.loads(b_request.decode())

        if validate_request(request):
            action_name = request.get('action')
            controller = resolve(action_name)
            if controller:
                try:
                    logging.info(f'Client send valid request {request}')
                    response = controller(request)
                except Exception as err:
 #                   logging.critical(f'Internal server error {err}')
                    response = make_response(request, 500, 'Internal server error')
            else:
 #               logging.error(f'Controller for {action_name} not found')
                response = make_response(request, 404, 'Action not found')
        else:
#            logging.error(f'Client send invalid request {request}')
            response = make_response(request, 400, 'Wrong request')

        str_response = json.dumps(response)
        client.send(str_response.encode())

        print(f'Client send message { b_request.decode() }')

        client.send(b_request)
        client.close()
except KeyboardInterrupt:
    logging.info('Server shutdown.')