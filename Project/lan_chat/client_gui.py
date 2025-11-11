import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# ---------- Configuration ----------
HOST = '10.125.212.23'   # 🔹 Replace with your server's IP
PORT = 55555

# ---------- Socket Setup ----------
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("LAN Chat - WhatsApp Style")
root.geometry("400x550")
root.configure(bg="#ECE5DD")

# ---------- Chat Frame ----------
chat_frame = tk.Frame(root, bg="#ECE5DD")
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state='disabled',
                                      bg="#ECE5DD", fg="#000000", font=("Segoe UI", 10))
chat_area.pack(fill=tk.BOTH, expand=True)

# ---------- Message Entry ----------
entry_frame = tk.Frame(root, bg="#FFFFFF", bd=2)
entry_frame.pack(fill=tk.X, side=tk.BOTTOM)

msg_entry = tk.Entry(entry_frame, bg="#FFFFFF", fg="#000000", font=("Segoe UI", 11))
msg_entry.pack(fill=tk.X, padx=10, pady=8, ipady=5)

# ---------- Functions ----------
def add_message(msg, sender="other"):
    """Adds a styled message bubble"""
    chat_area.config(state='normal')
    timestamp = datetime.now().strftime("%H:%M")

    if sender == "you":
        chat_area.insert(tk.END, f"\n{' ' * 40}🟢 You ({timestamp}): {msg}\n", "right")
        chat_area.tag_configure("right", justify="right", background="#DCF8C6", wrap="word")
    else:
        chat_area.insert(tk.END, f"\n👤 Friend ({timestamp}): {msg}\n", "left")
        chat_area.tag_configure("left", justify="left", background="#FFFFFF", wrap="word")

    chat_area.config(state='disabled')
    chat_area.yview(tk.END)

def send_message(event=None):
    """Send message to server"""
    msg = msg_entry.get().strip()
    if msg:
        client.send(msg.encode('utf-8'))
        add_message(msg, sender="you")
        msg_entry.delete(0, tk.END)

def receive_messages():
    """Receive messages from server"""
    while True:
        try:
            msg = client.recv(1024).decode('utf-8')
            add_message(msg, sender="other")
        except:
            print("⚠️ Disconnected from server")
            client.close()
            break

# ---------- Bind Events ----------
msg_entry.bind("<Return>", send_message)

# ---------- Start Thread ----------
threading.Thread(target=receive_messages, daemon=True).start()

root.mainloop()
