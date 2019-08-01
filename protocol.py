from datetime import datetime
from decorators import write_server_log



def validate_request(request):
    if 'action' in request and 'time' in request:
        return True
    return False

@write_server_log
def make_response(request, code, data=None):
    return {
        'action': request.get('action'),
        'time': datetime.now().timestamp(),
        'code': code,
        'data': data
    }