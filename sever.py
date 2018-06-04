from cgi import parse_qs
import json
from game import new_game, guess
def application(environ):
    error = False
    if environ["REQUEST_METHOD"] != 'POST':
        rsponse = {'code':'error', 'msg':'wrongHTTP method'}
        error = True
    if not error:
        try:
            path = environ['PATH_INFO'].split('/')
            if len(path) == 2:
                method = path[1]
            else:
                response = {'code':'error', 'msg':'wrong API path method'}
                error = True
        except:
            response = {'cod':'error', 'msg':'wrong HTTP method'}
            error = True
    try:
        request_body_size = int(environ.get)
