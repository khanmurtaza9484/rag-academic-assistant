# RAG Academic Assistant

A Retrieval-Augmented Generation (RAG) based academic assistant that answers questions from academic PDFs using semantic search and Gemini AI.

## Features

* Ask questions from academic PDFs
* Semantic retrieval using embeddings
* Vector search with FAISS
* AI-generated answers grounded in document context
* Gemini API integration
* Supports academic notes and textbooks

## Tech Stack

* Python
* Gemini API
* Sentence Transformers
* FAISS
* Scikit-learn
* PyPDF
* dotenv

## Project Workflow

PDF → Chunking → Embeddings → Vector Search → Context Retrieval → Gemini Response

## Installation

Clone the repository:

```bash
git clone https://github.com/khanmurtaza9484/rag-academic-assistant.git
cd rag-academic-assistant
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
python rag_chat.py
```

## Example Questions

* What is breadth first search?
* What are intelligent agents?
* What is rationality?
* Explain bidirectional search.

## Future Improvements

* Multi-PDF support
* Web UI using Streamlit
* Faster retrieval with saved embeddings
* Better ranking and chunk retrieval

## Author

Mohammad Murtaza Khan
