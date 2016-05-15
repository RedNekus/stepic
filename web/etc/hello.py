CONFIG = {
    "mode": "wsgi",
    "working_dir": r"/home/box/web/hello.py",
    "python": r"/usr/bin/python3.4",
    "args": (
        r"--bind=0.0.0.0:8080",
        r"--workers = 16",
        r"hello.application")
}
def wsgi_application(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    #params = env['QUERY_STRING'].split('&')
    body = 'HELLO'
    #for i in params:
        #key, val = params[i].split('=')
       # body = body + key + '=' + val + '\n'
    start_response(status, headers)
    return [body]