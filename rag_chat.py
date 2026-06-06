from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from google import genai
from dotenv import load_dotenv
import faiss
import numpy as np
import os

# -------------------------
# Load API key
# -------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

# -------------------------
# Load PDF
# -------------------------

pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted


# -------------------------
# Chunk text
# -------------------------

chunk_size = 800

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

print(f"Total chunks: {len(chunks)}")


# -------------------------
# Load embedding model
# -------------------------

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded.")


# -------------------------
# Create embeddings
# -------------------------

print("Creating embeddings...")

chunk_embeddings = model.encode(chunks)

chunk_embeddings = np.array(chunk_embeddings).astype("float32")


# -------------------------
# Create FAISS index
# -------------------------

dimension = chunk_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(chunk_embeddings)

print("Knowledge base ready.")


# -------------------------
# Chat loop
# -------------------------

while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    # Query embedding
    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    # Retrieve top 3 chunks
    k = 3

    distances, indices = index.search(query_embedding, k)

    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n"

    # Prompt for Gemini
    prompt = f"""
You are an academic assistant.

Answer only using the provided context.

If answer is not found in context, say:
"I could not find the answer in the document."

Context:
{context}

Question:
{query}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    print("\nAI Answer:\n")

    print(response.text)