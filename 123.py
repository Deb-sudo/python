import sqlite3
import os
from flask import Flask, request

app = Flask(__name__)

# 🔥 VULNERABILITY 1: Hardcoded credentials
DB_PATH = 'users.db'
ADMIN_PASSWORD = 'supersecret123'  # Sensitive info hardcoded

# 🔥 VULNERABILITY 2: SQL Injection
@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print("[DEBUG] Executing:", query)  # Leaks info to logs
    cursor.execute(query)
    
    if cursor.fetchone():
        return "Login successful!"
    return "Invalid credentials"

# 🔥 VULNERABILITY 3: Command Injection
@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    output = os.popen(f"ping -c 1 {ip}").read()
    return f"<pre>{output}</pre>"

# 🔥 VULNERABILITY 4: Debug mode enabled (do not do this in prod!)
if __name__ == '__main__':
    app.run(debug=True)
