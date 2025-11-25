import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# -------------------- Configuration --------------------
SERVER_IP = input("Enter server IP (e.g. 192.168.56.1): ").strip()
PORT = 5555

# Create socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((SERVER_IP, PORT))
except Exception as e:
    print("❌ Unable to connect to the server:", e)
    exit()

username = input("Enter your username: ").strip()
client.send(username.encode('utf-8'))


# -------------------- Tkinter Window Setup --------------------
root = tk.Tk()
root.title(f"LAN Chat - {username}")
root.geometry("500x500")
root.config(bg="#20232A")

chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#282C34", fg="white", font=("Consolas", 11))
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_display.config(state=tk.DISABLED)

message_entry = tk.Entry(root, bg="#3B4048", fg="white", font=("Consolas", 11))
message_entry.pack(fill=tk.X, padx=10, pady=(0, 10))
message_entry.focus()


# -------------------- Functions --------------------
def receive_messages():
    """Continuously receive messages from the server."""
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if not message:
                break
            chat_display.config(state=tk.NORMAL)
            chat_display.insert(tk.END, message + "\n")
            chat_display.yview(tk.END)
            chat_display.config(state=tk.DISABLED)
        except:
            break


def send_message(event=None):
    """Send the typed message to the server."""
    message = message_entry.get().strip()
    if not message:
        return

    if message == "/exit":
        client.send(message.encode('utf-8'))
        client.close()
        root.destroy()
        return

    try:
        client.send(message.encode('utf-8'))
        message_entry.delete(0, tk.END)
    except:
        messagebox.showerror("Error", "Unable to send message. Connection lost.")
        root.destroy()


def on_close():
    """Handle window close event."""
    try:
        client.send("/exit".encode('utf-8'))
    except:
        pass
    client.close()
    root.destroy()


# -------------------- Bindings --------------------
message_entry.bind("<Return>", send_message)
root.protocol("WM_DELETE_WINDOW", on_close)

# -------------------- Start Receiving Thread --------------------
receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

# -------------------- Run GUI --------------------
root.mainloop()
