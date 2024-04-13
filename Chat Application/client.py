import socket
import threading

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode())
        if message == "/quit":
            break

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode()
        print(message)
        if message == "/quit":
            break

def start_client(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    send_thread = threading.Thread(target=send_message, args=(client,))
    receive_thread = threading.Thread(target=receive_messages, args=(client,))

    send_thread.start()
    receive_thread.start()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345

    start_client(HOST, PORT)
