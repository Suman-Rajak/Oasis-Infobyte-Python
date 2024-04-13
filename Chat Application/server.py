import socket
import threading

def handle_client(client_socket, client_address, clients):
    print(f"[NEW CONNECTION] {client_address} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message == "/quit":
                print(f"[DISCONNECTED] {client_address} disconnected.")
                client_socket.close()
                clients.remove(client_socket)
                break
            print(f"[{client_address}] {message}")

            # Broadcast the message to all clients
            broadcast_message(message, client_socket, clients)
        except ConnectionResetError:
            print(f"[DISCONNECTED] {client_address} forcibly disconnected.")
            client_socket.close()
            clients.remove(client_socket)
            break

def broadcast_message(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[LISTENING] Server is listening on {host}:{port}")

    clients = []

    while True:
        client_socket, client_address = server.accept()
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address, clients))
        client_thread.start()

if __name__ == "__main__":
    HOST = "127.0.0.1"  # localhost
    PORT = 12345

    start_server(HOST, PORT)
