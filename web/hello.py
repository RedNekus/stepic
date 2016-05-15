CONFIG = {
    "mode": "wsgi",
    "working_dir": "/home/box/web/hello.py",
    "args": (
        "--bind=0.0.0.0:8080",
        "--workers = 16",
        "hello.app")
}
def app(environment, response):
    params=environment["QUERY_STRING"].replace("&","\n")
    headers=[("Content-Type", "text/plain")]
    response("200 OK", headers)
    return [params]