# 📚 AI PDF Q&A Chatbot (RAG)

A **Retrieval-Augmented Generation (RAG)** based PDF Question Answering chatbot built using **Python**, **FAISS**, **Sentence Transformers**, **Google Gemini**, and **Streamlit**.

The application allows users to upload one or more PDF documents, retrieve the most relevant information using semantic vector search, and generate accurate answers grounded in the uploaded documents.

---

# 🚀 Live Demo

**Hugging Face Space**

👉 https://huggingface.co/spaces/khanmurtaza/rag-academic-assistant

---

# ✅ Project Status

### Completed Features

- ✅ Multiple PDF Upload
- ✅ PDF Text Extraction
- ✅ Automatic Text Chunking
- ✅ Semantic Search using FAISS
- ✅ Google Gemini Integration
- ✅ Streamlit Web Interface
- ✅ Hugging Face Deployment
- ✅ Modular Project Architecture

---

# ✨ Features

- Upload one or more PDF documents
- Automatic PDF text extraction
- Intelligent text chunking
- Semantic embeddings using Sentence Transformers
- Fast similarity search using FAISS
- Google Gemini powered answer generation
- Multi-document question answering
- Streamlit web interface
- Docker deployment on Hugging Face Spaces
- Modular and extensible project structure

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF
- NumPy
- python-dotenv
- Docker
- Git
- GitHub
- Hugging Face Spaces

---

# 📂 Project Structure

```text
rag-academic-assistant/
│
├── app.py
├── rag_chat.py
├── Dockerfile
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
└── test_*.py
```

---

# ⚙️ How It Works

1. Upload one or more PDF documents.
2. Extract text from each document.
3. Split the extracted text into manageable chunks.
4. Generate embeddings using Sentence Transformers.
5. Store embeddings inside a FAISS vector index.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks using similarity search.
8. Send the retrieved context to Google Gemini.
9. Generate and display the final answer.

---

# 🧠 RAG Architecture

```text
               PDF Upload
                    │
                    ▼
          Text Extraction
                    │
                    ▼
              Text Chunking
                    │
                    ▼
      Sentence Transformer Embeddings
                    │
                    ▼
            FAISS Vector Index
                    │
                    ▼
             User Question
                    │
                    ▼
      Semantic Similarity Search
                    │
                    ▼
          Relevant Text Chunks
                    │
                    ▼
          Google Gemini LLM
                    │
                    ▼
             Final Response
```

---

# ⚡ Installation

Clone the repository

```bash
git clone https://github.com/khanmurtaza9484/rag-academic-assistant.git
```

Navigate into the project

```bash
cd rag-academic-assistant
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Screenshots

## Home Page

![Home](screenshots/home.png)

---

## Uploading PDF Documents

![Upload](screenshots/upload.png)

---

## Asking Questions

![Question](screenshots/question.png)

---

## AI Generated Answer

![Answer](screenshots/answer.png)

---

## Multiple PDF Support

![Multiple PDFs](screenshots/multiple_pdfs.png)

---

# 🔮 Future Improvements

- Display source citations with page numbers
- Persistent FAISS index
- Conversation history
- OCR support for scanned PDFs
- Hybrid keyword + semantic search
- Improved UI/UX
- Authentication for private document collections

---

# 👨‍💻 Author

**Mohammad Murtaza Khan**

GitHub: https://github.com/khanmurtaza9484

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

# 📄 License

This project is licensed under the **MIT License**.