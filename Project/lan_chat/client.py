import socket
import threading

# -------------------- Configuration --------------------
SERVER_IP = input("Enter server IP (e.g. 192.168.1.10): ").strip()
PORT = 5555

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

# Ask for username
username = input("Enter your username: ")
client.send(username.encode('utf-8'))

print(f"✅ Connected to chat server as {username}")
print("Type '/exit' to leave the chat.\n")


# -------------------- Receiving Messages --------------------
def receive_messages():
    """Continuously receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            print("⚠️ Disconnected from server.")
            client.close()
            break


# -------------------- Sending Messages --------------------
def send_messages():
    """Continuously read input and send messages."""
    while True:
        message = input()
        if message.strip() == '/exit':
            client.send(message.encode('utf-8'))
            print("🚪 You left the chat.")
            client.close()
            break
        try:
            client.send(message.encode('utf-8'))
        except:
            print("⚠️ Message failed to send.")
            break


# -------------------- Threads --------------------
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

send_messages()
