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




import os
import PyPDF2
from chromadb import ChromaDB
from langchain import Langchain
from langchain.llms import GPT4o

class PDFRAG:
    def __init__(self, pdf_directory, chroma_db_path):
        self.pdf_directory = pdf_directory
        self.chroma_db = ChromaDB(chroma_db_path)
        self.langchain = Langchain()
        self.llm = GPT4o()

    def extract_text_from_pdfs(self):
        documents = []
        for filename in os.listdir(self.pdf_directory):
            if filename.endswith('.pdf'):
                filepath = os.path.join(self.pdf_directory, filename)
                with open(filepath, 'rb') as pdf_file:
                    reader = PyPDF2.PdfReader(pdf_file)
                    text = ''
                    for page in reader.pages:
                        text += page.extract_text()
                    documents.append({'title': filename, 'content': text})
        return documents

    def store_documents_in_chromadb(self, documents):
        for doc in documents:
            # Ensure each document is added to ChromaDB
            self.chroma_db.add_document(doc['title'], doc['content'])

    def generate_response(self, query):
        # Use Langchain to create a retrieval chain
        retrieval_chain = self.langchain.create_chain(self.chroma_db, self.llm)
        response = retrieval_chain.run(query)
        return response

    def run_rag_pipeline(self, query):
        documents = self.extract_text_from_pdfs()
        self.store_documents_in_chromadb(documents)
        return self.generate_response(query)

# Usage example
rag = PDFRAG(pdf_directory='./pdfs', chroma_db_path='./chroma_db')
response = rag.run_rag_pipeline(query='What is the main topic in these documents?')
print(response)





# explain the ingestion pipeline in RAG_SYN





# Requirement: Implement RAG over PDF documents using ChromaDB, Langchain, and GPT-4o in Python.

import os
import PyPDF2
from chromadb import ChromaDB
from langchain import Langchain
from gpt4o import GPT4o

class PDFRAGSystem:
    def __init__(self, pdf_directory):
        self.pdf_directory = pdf_directory
        self.chroma_db = ChromaDB()
        self.langchain = Langchain()
        self.gpt4o = GPT4o()

    def load_pdfs(self):
        pdf_files = [f for f in os.listdir(self.pdf_directory) if f.endswith('.pdf')]
        documents = {}
        for pdf_file in pdf_files:
            pdf_path = os.path.join(self.pdf_directory, pdf_file)
            try:
                with open(pdf_path, 'rb') as file:
                    pdf_reader = PyPDF2.PdfReader(file)
                    text = ''
                    for page in range(len(pdf_reader.pages)):
                        text += pdf_reader.pages[page].extract_text() or ''
                documents[pdf_file] = text
            except Exception as e:
                print(f"Error reading {pdf_file}: {e}")
        return documents

    def index_documents(self, documents):
        for title, content in documents.items():
            self.chroma_db.index_document(title, content)

    def query_documents(self, query):
        # Retrieve relevant documents
        results = self.chroma_db.query(query)
        # Use Langchain to refine the results
        refined_results = self.langchain.process_results(results)
        # Generate final output with GPT-4o
        final_output = self.gpt4o.generate_response(refined_results)
        return final_output

    def execute_query(self, query):
        documents = self.load_pdfs()
        self.index_documents(documents)
        return self.query_documents(query)

# Usage example:
# pdf_rag_system = PDFRAGSystem(pdf_directory='/path/to/pdf/files')
# response = pdf_rag_system.execute_query('What is the content about?')
# print(response)

# Note: This code assumes that ChromaDB, Langchain, and GPT4o libraries have appropriate methods such as
# `index_document`, `query`, `process_results`, and `generate_response` implemented.


# What are the features and architecture for aks cluster


# explain the ingestion pipeline in RAG_SYN
# Requirement: Implement RAG over PDF documents using ChromaDB, Langchain, and GPT-4o in Python.


# What is soot diff process of comparing java programs
 
# What are the features and architecture for aks cluster

explain leave policy

What is dry lab