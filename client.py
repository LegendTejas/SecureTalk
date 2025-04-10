import socket
import threading

# Client configuration
HOST = '127.0.0.1'
PORT = 5555 

# Create client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Ask for a username at the start
username = input("Enter your username: ")
client.send(username.encode())  # Sending username to server

# Function to receive messages
def receive_messages():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print(msg)
        except:
            print("Disconnected from server.")
            client.close()
            break

# Start receiving messages in a separate thread
threading.Thread(target=receive_messages, daemon=True).start()

# Sending messages loop
while True:
    receiver = input("Enter recipient username: ")
    message = input("Enter message: ")
    
    if receiver and message:  # Ensure inputs are not empty
        full_message = f"{username}:{receiver}:{message}"  # Format message as "sender:receiver:message"
        client.send(full_message.encode())  # Send message to server
    else:
        print("Both receiver and message must be provided!")

        