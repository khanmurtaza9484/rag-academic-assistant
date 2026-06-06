from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# -------------------------
# STEP 1: Load PDF
# -------------------------

pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

reader = PdfReader(pdf_path)

text = ""

for page in reader.pages:
    extracted = page.extract_text()
    if extracted:
        text += extracted


# -------------------------
# STEP 2: Chunk text
# -------------------------

chunk_size = 800

chunks = [
    text[i:i + chunk_size]
    for i in range(0, len(text), chunk_size)
]

print(f"Total chunks: {len(chunks)}")


# -------------------------
# STEP 3: Load embedding model
# -------------------------

print("Loading model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model loaded.")


# -------------------------
# STEP 4: Convert chunks to embeddings
# -------------------------

print("Creating embeddings...")

chunk_embeddings = model.encode(chunks)

chunk_embeddings = np.array(chunk_embeddings).astype("float32")


# -------------------------
# STEP 5: Create FAISS index
# -------------------------

dimension = chunk_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(chunk_embeddings)

print("Knowledge base ready.")


# -------------------------
# STEP 6: Ask Question
# -------------------------

while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    query_embedding = model.encode([query])

    query_embedding = np.array(query_embedding).astype("float32")

    k = 3

    distances, indices = index.search(query_embedding, k)

    context = ""

    print("\nRetrieved Chunks:\n")

    for idx in indices[0]:
        print("-" * 50)
        print(chunks[idx][:500])
        print()

        context += chunks[idx] + "\n"

    print("\nFinal Context Ready.")