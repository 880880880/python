import logging
from functools import wraps
from settings import SERVER_LOGS

logger = logging.getLogger('decorators')


def logged(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        logger.debug(f'{func.__name__}: {request}')
        return func(request, *args, **kwargs)
    return wrapper



def write_server_log(func):   # decorates make_response
    @wraps(func)
    def writer(request, code, *args, **kwargs):
        log_level = SERVER_LOGS[code]['level']
        log_string = 'CODE: ' + str(code) + ' - ' + func.__name__ + ': ' + SERVER_LOGS[code]['message']
        if log_level == 10:
            logger.debug(log_string)
        elif log_level == 20:
            logger.info(log_string)
        elif log_level == 30:
            logger.warning(log_string)
        elif log_level == 40:
            logger.error(log_string)
        else:
            logger.critical(log_string)
        return func(request, *args, **kwargs)
    return writer
