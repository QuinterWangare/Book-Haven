import sqlite3
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('contact_submissions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact_submissions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            submission_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Route to handle form submissions
@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    try:
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Validate input
        if not all([name, email, message]):
            return jsonify({'error': 'All fields are required'}), 400

        # Connect to database and insert submission
        conn = sqlite3.connect('contact_submissions.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO contact_submissions (name, email, message) 
            VALUES (?, ?, ?)
        ''', (name, email, message))
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'message': 'Message submitted successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Initialize database when the app starts
if __name__ == '__main__':
    init_db()
    app.run(debug=True)