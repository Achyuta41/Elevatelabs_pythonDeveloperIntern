import socket
import threading
from datetime import datetime

# -------------------- Server Configuration --------------------
HOST = '0.0.0.0'   # Listen on all network interfaces
PORT = 5555        # You can choose any unused port > 1024

# Create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"✅ Server started on 198.168.56.1 :{PORT}")
print("Waiting for clients to connect...")

clients = []        # To store all connected client sockets
usernames = {}      # To map client sockets -> usernames


# -------------------- Broadcast Function --------------------
def broadcast(message, sender_socket=None):
    """Send message to all connected clients except the sender."""
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                remove_client(client)


# -------------------- Remove Client --------------------
def remove_client(client):
    """Remove disconnected client from list."""
    if client in clients:
        clients.remove(client)
        username = usernames.get(client, "Unknown")
        del usernames[client]
        print(f"❌ {username} disconnected.")


# -------------------- Handle Each Client --------------------
def handle_client(client_socket):
    """Handle messages from a single client."""
    # Step 1: Receive username
    username = client_socket.recv(1024).decode('utf-8')
    usernames[client_socket] = username
    clients.append(client_socket)

    print(f"👤 {username} connected.")
    broadcast(f"📢 {username} joined the chat!", client_socket)

    # Step 2: Keep listening for messages
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            if not message:
                break  # client closed connection

            # Handle /exit command
            if message.strip() == '/exit':
                broadcast(f"🚪 {username} has left the chat.")
                remove_client(client_socket)
                break

            # Add timestamp & write to log
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_message = f"[{timestamp}] {username}: {message}\n"

            with open("chat_log.txt", "a") as log_file:
                log_file.write(log_message)

            # Broadcast to all
            broadcast(f"{username}: {message}", client_socket)

        except Exception as e:
            print(f"⚠️ Error with {username}: {e}")
            remove_client(client_socket)
            break

    client_socket.close()


# -------------------- Accept Connections --------------------
def accept_connections():
    """Main loop to accept clients."""
    while True:
        client_socket, client_address = server.accept()
        print(f"🔗 Connected with {client_address}")

        # Create a new thread for each client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()


# -------------------- Main Execution --------------------
if __name__ == "__main__":
    accept_connections()
