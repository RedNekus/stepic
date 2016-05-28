import math
def app(environment, response):
    params=environment["QUERY_STRING"].replace("&","\n")
    headers=[("Content-Type", "text/plain")]
    response("200 OK", headers)
    return [params]