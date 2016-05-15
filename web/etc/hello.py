CONFIG = {
    "mode": "wsgi",
    "working_dir": "/home/box/web/hello.py",
    "python": "/usr/bin/python3.4",
    "args": (
        "--bind=0.0.0.0:8080",
        "--workers = 16",
        "hello.application")
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