import socket
import threading
def server(conn, a):
        while True:
                data = conn.recv(1024)
                if not data or data == 'close': break
                conn.send(data)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
while True:
        connector, address = s.accept()
        print('Connection', address)
        t = threading.Thread(target=server, args=(connector, address))
        t.start()
connector.close()
