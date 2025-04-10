#Step 1: Install Required Libraries (pip install mysql-connector-python pycryptodome)

#Step 2: MySQL Database Setup
import mysql.connector as myConn

# MySQL Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "tejas969959",
    "auth_plugin": "mysql_native_password"
}

# Connect to MySQL Server
mydb = myConn.connect(**db_config) #Establishes a connection to MySQL using the details from db_config
db_cursor = mydb.cursor() #Creates a cursor object (db_cursor) which is used to execute SQL statements

# Create Database
db_cursor.execute("CREATE DATABASE IF NOT EXISTS secure_chat")
db_cursor.execute("USE secure_chat")

# Create Messages Table
db_cursor.execute("""
         CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        sender VARCHAR(255),
        receiver VARCHAR(255),
        encrypted_message TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Check and Create Index for Efficient Searching
db_cursor.execute("SHOW INDEX FROM messages WHERE Key_name = 'idx_receiver'")
if not db_cursor.fetchall():
    db_cursor.execute("CREATE INDEX idx_receiver ON messages(receiver)")

# Check and Enable Full-Text Search (Avoiding Duplicates)
db_cursor.execute("SHOW INDEX FROM messages WHERE Key_name = 'encrypted_message_fulltext'")
if not db_cursor.fetchall():
    db_cursor.execute("ALTER TABLE messages ADD FULLTEXT INDEX encrypted_message_fulltext (encrypted_message)")

# Commit Changes and Close Connection
mydb.commit()
mydb.close()

print("✓ Database and Table Setup Completed Successfully!")