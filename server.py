import socket
import threading
def server(conn, a):
        while True:
                data = conn.recv(1024)
                if not data or data == 'close': break
                conn.send(data)
        conn.close()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
for i in range(9):
        connector, address = s.accept()
        print('Connection', i, address)
        t = threading.Thread(target=server, args=(connector, address))
        t.start()

