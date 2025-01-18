import sqlite3
import os
import requests
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable to SQL Injection
def vulnerable_sql_injection(user_input):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"  # Unsafe query
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Vulnerable to XSS
@app.route('/xss', methods=['GET'])
def vulnerable_xss():
    user_input = request.args.get('input')
    template = f"<h1>User Input: {user_input}</h1>"  # Unsafe HTML rendering
    return render_template_string(template)

# Vulnerable to SSRF
@app.route('/ssrf', methods=['GET'])
def vulnerable_ssrf():
    url = request.args.get('url')
    response = requests.get(url)  # Unsafe URL fetching
    return response.text

# Vulnerable to File Inclusion
@app.route('/file', methods=['GET'])
def vulnerable_file_inclusion():
    filename = request.args.get('file')
    with open(filename, 'r') as file:  # Unsafe file access
        return file.read()

# Vulnerable to Command Injection
@app.route('/command', methods=['GET'])
def vulnerable_command_injection():
    cmd = request.args.get('cmd')
    result = os.popen(cmd).read()  # Unsafe command execution
    return result

# Flask Route for SQL Injection Testing
@app.route('/sql', methods=['GET'])
def sql_route():
    user_input = request.args.get('username')
    results = vulnerable_sql_injection(user_input)
    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
