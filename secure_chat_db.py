#Step 3: AES Encryption & MySQL Connection 
import mysql.connector
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tejas969959", 
    "database": "secure_chat",
    "auth_plugin": "mysql_native_password"
}

# Secret key (Must be 16, 24, or 32 bytes)
SECRET_KEY = b"thisisverysecret"  # 16-byte key

# AES Encryption Function
def encrypt_message(message):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(message.encode(), AES.block_size))
    return base64.b64encode(iv + encrypted_data).decode()

# AES Decryption Function
def decrypt_message(encrypted_message):
    raw_data = base64.b64decode(encrypted_message)
    iv = raw_data[:AES.block_size]
    encrypted_data = raw_data[AES.block_size:]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data), AES.block_size).decode()

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(**db_config)

print("✓ Connected to MySQL Database")
