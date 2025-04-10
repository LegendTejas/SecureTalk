#Step 4: Store & Retrieve Messages

from secure_chat_db import connect_db, encrypt_message, decrypt_message

# Store Encrypted Messages in MySQL
def store_message(sender, receiver, message):
    db = connect_db()
    cursor = db.cursor()
    
    encrypted_message = encrypt_message(message)
    sql = "INSERT INTO messages (sender, receiver, encrypted_message) VALUES (%s, %s, %s)"
    cursor.execute(sql, (sender, receiver, encrypted_message))
    
    db.commit()
    db.close()

# Retrieve Messages with Full-Text Search & Pagination
def get_messages(receiver, search_query=None, limit=10, offset=0):
    db = connect_db()
    cursor = db.cursor()
    
    if search_query:
        sql = """SELECT sender, encrypted_message, timestamp 
                 FROM messages 
                 WHERE receiver = %s AND MATCH(encrypted_message) AGAINST (%s IN NATURAL LANGUAGE MODE) 
                 ORDER BY timestamp DESC LIMIT %s OFFSET %s"""
        cursor.execute(sql, (receiver, search_query, limit, offset))
    else:
        sql = """SELECT sender, encrypted_message, timestamp 
                 FROM messages 
                 WHERE receiver = %s ORDER BY timestamp DESC LIMIT %s OFFSET %s"""
        cursor.execute(sql, (receiver, limit, offset))
    
    results = cursor.fetchall()
    db.close()

    decrypted_messages = [(sender, decrypt_message(enc_msg), timestamp) for sender, enc_msg, timestamp in results]
    return decrypted_messages

print("✓ Message storage and retrieval ready")