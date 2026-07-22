import streamlit as st
import os

from google import genai
from dotenv import load_dotenv

from src.pdf_loader import extract_text
from src.chunker import create_chunks
from src.vector_store import create_vector_store

# -------------------------
# Load Gemini API
# -------------------------

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -------------------------
# Page Configuration
# -------------------------

st.set_page_config(
    page_title="AI PDF Q&A Chatbot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI PDF Q&A Chatbot")
st.write("Upload one or more PDF documents and ask questions about them.")

# -------------------------
# Upload PDFs
# -------------------------

uploaded_files = st.file_uploader(
    "Upload PDF Documents",
    type="pdf",
    accept_multiple_files=True
)

# -------------------------
# Build Knowledge Base
# -------------------------

if uploaded_files:

    os.makedirs("documents", exist_ok=True)

    all_text = ""

    for uploaded_file in uploaded_files:

        pdf_path = os.path.join("documents", uploaded_file.name)

        with open(pdf_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        text = extract_text(pdf_path)

        all_text += text + "\n"

    st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully!")

    # Create chunks
    chunks = create_chunks(all_text)

    # Create ChromaDB Vector Store
    model, collection = create_vector_store(chunks)

    # -------------------------
    # Ask Question
    # -------------------------

    question = st.text_input("Ask a question")

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            # Convert question into embedding
            query_embedding = model.encode([question]).tolist()

            # Retrieve relevant chunks
            results = collection.query(
                query_embeddings=query_embedding,
                n_results=3
            )

            context = "\n".join(results["documents"][0])

            # Prompt
            prompt = f"""
You are an academic assistant.

Answer the user's question using ONLY the information provided in the context.

If the information is partially available, answer as completely as possible from the context.

Do NOT use outside knowledge.

Only reply "I could not find the answer in the document." if the context contains no relevant information at all.

Context:
{context}

Question:
{question}
"""

            try:

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                st.subheader("Answer")
                st.write(response.text)

            except Exception as e:

                st.error(f"Error: {e}")