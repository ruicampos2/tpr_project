import socket
import threading

def send_requrest(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n"
            s.sendall(request.encode())
    except Exception as e:
        print(f"Erro: {e}")

host = "192.168.100.5"
port = 5000
threads = 100

for _ in range(threads):
    threading.Thread(target=send_requrest, args=(host, port)).start()