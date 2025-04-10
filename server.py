#Step 5: Server Code
import socket
import threading
from secure_chat_db import connect_db, encrypt_message  # Import DB functions

# Server configuration
HOST = '127.0.0.1'
PORT = 5555

clients = {}  # Dictionary to store connected clients

# Function to handle client connections
def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    
    try:
        username = client_socket.recv(1024).decode()  # Receive username
        clients[username] = client_socket
        print(f"[USERNAME] {username} joined the chat.")

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break

            print(f"[MESSAGE RECEIVED] {addr}: {data}")

            # Extract sender, receiver, and message
            parts = data.split(":", 2)  # Expecting "sender:receiver:message"
            if len(parts) != 3:
                print("[ERROR] Invalid message format")
                continue
            
            sender, receiver, message = parts
            encrypted_msg = encrypt_message(message)  # Encrypt message

            # Store message in MySQL
            db = connect_db()
            cursor = db.cursor()
            query = "INSERT INTO messages (sender, receiver, encrypted_message) VALUES (%s, %s, %s)"
            cursor.execute(query, (sender, receiver, encrypted_msg))
            db.commit()
            cursor.close()
            db.close()
            print("[MESSAGE STORED]")

            # Forward message to the intended recipient
            if receiver in clients:
                try:
                    clients[receiver].send(f"{sender}: {message}".encode())
                except:
                    print(f"[ERROR] Could not send message to {receiver}")

    except Exception as e:
        print(f"[ERROR] {e}")

    print(f"[DISCONNECTED] {addr} left.")
    del clients[username]
    client_socket.close()

# Function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[LISTENING] Server is running on {HOST}:{PORT}")

    while True:
        try:
            client_socket, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, addr))
            thread.start()
        except Exception as e:
            print(f"[SERVER ERROR] {e}")

# Start the server
if __name__ == "__main__":
    start_server()