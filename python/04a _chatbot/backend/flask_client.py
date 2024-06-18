from talk_to_gpt_4o import get_completion
import os
from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')


def get_db_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'chat.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_chat_history', methods=['GET'])
def get_chat_history():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM messages ORDER BY id').fetchall()
    conn.close()
    message_list = [{'sender': msg['sender'], 'message': msg['message'], 'timestamp': msg['timestamp']} for msg in messages]
    return jsonify({'messages': message_list})

@app.route('/chat', methods=['POST'])
def chat():
    customer_message = request.json['message'].strip()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        return jsonify({'response': 'API Key not found. Please set the OPENAI_API_KEY environment variable.'})

    # Process the customer's message using GPT4O
    gpt4o_response = get_completion(customer_message)

    # Store user message
    conn = get_db_connection()
    conn.execute('INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)', ('user', customer_message, timestamp))
    conn.execute('INSERT INTO messages (sender, message, timestamp) VALUES (?, ?, ?)', ('bot', gpt4o_response, timestamp))
    conn.commit()
    conn.close()
    return {'response': gpt4o_response}

@app.route('/clear_chat_history', methods=['POST'])
def clear_chat_history():
    conn = get_db_connection()
    conn.execute('DELETE FROM messages')
    conn.commit()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run()
