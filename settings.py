INSTALLED_APPS = [
    'echo',
    'messenger'
]

SERVER_LOGS = {
    200: {'level': 20, 'message': 'OK'},
    400: {'level': 40, 'message': 'Wrong request'},
    404: {'level': 40, 'message': 'Action not found'},
    500: {'level': 50, 'message': 'Internal server error'}
}