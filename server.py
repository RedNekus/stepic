import socket
def server(conn):
        while True:
                data = conn.recv(1024)
                if not data or data == 'close': break
                conn.send(data)
        conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
while True:
        conn, addr = s.accept()
        print('Connection', addr)
        t = threading.Thread(target=server, args=(conn, addr))
        t.start()
