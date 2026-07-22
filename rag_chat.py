# Import project modules
from src.pdf_loader import extract_text
from src.chunker import create_chunks
from src.vector_store import create_vector_store

# Import required libraries
from google import genai
from dotenv import load_dotenv
import os

# -------------------------
# Load API Key
# -------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# -------------------------
# Load PDF
# -------------------------

pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

text = extract_text(pdf_path)

chunks = create_chunks(text)

print(f"Total chunks: {len(chunks)}")

# -------------------------
# Create Vector Store
# -------------------------

model, collection = create_vector_store(chunks)

# -------------------------
# Chat Loop
# -------------------------

while True:

    query = input("\nAsk a question (type 'exit' to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
You are an academic assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, reply exactly:

"I could not find the answer in the document."

Context:
{context}

Question:
{query}
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("\nAI Answer:\n")
        print(response.text)

    except Exception as e:

        print("\nError generating response:")
        print(e)