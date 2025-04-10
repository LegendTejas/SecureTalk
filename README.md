# SecureTalk
![image](https://github.com/user-attachments/assets/b61676c1-ddd3-4332-9c24-bacdde084adc)

A real-time, encrypted chat application built using Python sockets, AES encryption, and MySQL for secure message storage.

**OVERVIEW**
This project is a secure, terminal-based chat system designed to ensure private communication between users. It uses AES encryption to protect message content and stores encrypted messages in a MySQL database. The application supports real-time messaging with a multithreaded server capable of handling multiple clients simultaneously.

**FEATURES**
* AES Encryption (CBC mode) for secure message transmission
* Real-time messaging using Python socket and threading
* Secure storage of encrypted messages in MySQL
* Full-text search and pagination for efficient message retrieval
* Modular code structure for easy maintenance

**🧰 Tech Stack**
* Language: Python
* Encryption: AES (PyCryptodome)
* Database: MySQL
* Networking: Python socket & threading


**💻 How to Run**
1. Step 1: install modules
`pip install mysql-connector-python pycryptodome`

2. Step 2: Run setup_db.py file and set up MySQL Database

3. Step 3: AES Encryption & MySQL Connection Run secure_chat_db.py file

4. Step 4: Run store_retrieve.py file

5. Step 5: Start Server i.e. run server.py file

6. Step 6: Once the server starts listening then start Client run client.py file and when the connection is established the message will be shown in the Server and we can enter username in the client file and start messaging

7. Step 7: After everything is done the encrypted message will be stored in the MySQL Database and no one will be able to decrypt the messages easily. 
