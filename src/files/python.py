# Import necessary libraries
import threading
import sqlite3
from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Flask App Setup
app = Flask(__name__)

# Basic Route
@app.route('/')
def home():
    return jsonify(message="Welcome to the Python Sample App!")

# REST API Example
@app.route('/api/v1/greet', methods=['POST'])
def greet():
    data = request.json
    name = data.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")

# 
# Multithreading Example Function in Python
import threading

def print_hello():
    print("Hello from a thread!")

# Create a thread
thread = threading.Thread(target=print_hello)

# Start the thread
thread.start()

# Wait for the thread to complete
thread.join()
def print_numbers():
    for i in range(1, 6):
        print(f"Thread: {i}")

# Database Setup and Operations
def setup_database():
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            name TEXT, 
            age INTEGER
        )
    ''')
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Alice", 25))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Bob", 30))
    connection.commit()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    connection.close()
    return rows

# Consume an API
def fetch_api_data():
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    if response.status_code == 200:
        return response.json()
    return {"error": "Failed to fetch data"}

# Web Scraping Example
def scrape_website():
    url = "https://example.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string
    return "Failed to scrape"

# Generate PDF Example
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sample PDF Content", ln=True, align='C')
    pdf.output("sample.pdf")
    return "PDF generated successfully!"

# Main Execution
if __name__ == '__main__':
    # Run Flask App in a Thread
    flask_thread = threading.Thread(target=lambda: app.run(debug=True, use_reloader=False))
    # flask_thread.start()
    thread = threading.Thread(target=print_numbers)
    thread.start()
    thread.join()
    print("Database Data:")
    users = setup_database()
    for user in users:
        print(user)
    print("\nAPI Data:")
    api_data = fetch_api_data()
    print(api_data)
    print("\nScraped Website Title:")
    print(scrape_website()) 
    print("\nPDF Creation:")
    print(create_pdf())
    flask_thread.join()

    
# explain the genrate_answer function


# get the record_audio_chunk function code

# what are the use cases for genie



