def wsgi_application(env, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/plain')]
    params = env['QUERY_STRING'].split('&')
    body = ''
    for i in params:
        key, val = params[i].split('=')
        body = body + key + '=' + val + '\n'
    start_response(status, headers)
    return body