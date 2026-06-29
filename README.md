# 📚 AI PDF Q&A Chatbot (RAG)

A Retrieval-Augmented Generation (RAG) based PDF Question Answering chatbot built using **Python**, **FAISS**, **Sentence Transformers**, **Google Gemini**, and **Streamlit**.

The application allows users to upload one or more PDF documents, ask questions in natural language, retrieve the most relevant document sections using vector search, and generate answers grounded in the uploaded documents.

---

## Features

* Upload one or more PDF documents
* Extract text from PDFs
* Automatic text chunking
* Semantic embeddings using Sentence Transformers
* FAISS vector similarity search
* Google Gemini powered answer generation
* Streamlit web interface
* Modular project structure
* Easy to extend with additional features

---

## Technologies Used

* Python
* Streamlit
* Google Gemini API
* Sentence Transformers
* FAISS
* PyPDF
* NumPy
* python-dotenv

---

## Project Structure

```text
rag-academic-assistant/
│
├── app.py
├── rag_chat.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── src/
│   ├── pdf_loader.py
│   ├── chunker.py
│   └── vector_store.py
│
├── screenshots/
│
├── documents/
│
└── test_*.py
```

---

## How It Works

1. Upload one or more PDF files.
2. Extract text from each document.
3. Split the text into manageable chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in a FAISS vector database.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks.
8. Send the retrieved context to Google Gemini.
9. Display the generated answer.

---

## RAG Architecture

```text
PDF Upload
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Sentence Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
User Question
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context
      │
      ▼
Google Gemini
      │
      ▼
Final Answer
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/khanmurtaza9484/rag-academic-assistant.git
```

Navigate to the project:

```bash
cd rag-academic-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

![Home](screenshots/home.png)

### Uploading PDFs

![Upload](screenshots/upload.png)

### Asking Questions
![Question](screenshots/question.png)

### Giving Answers
![Answer](screenshots/answer.png)

### Multiple PDF Support

![Multiple PDFs](screenshots/multiple_pdfs.png)

---

## Future Improvements

* Source citations with page numbers
* Conversation history
* OCR support for scanned PDFs
* Hybrid keyword + vector search
* ChromaDB integration
* Hugging Face deployment

---

## Author

**Mohammad Murtaza Khan**

GitHub: https://github.com/khanmurtaza9484
