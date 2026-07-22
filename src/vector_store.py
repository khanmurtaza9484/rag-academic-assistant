import chromadb
from sentence_transformers import SentenceTransformer


def create_vector_store(chunks):
    """
    Creates embeddings for text chunks and stores them
    in a ChromaDB vector database.

    Args:
        chunks (list): List of text chunks.

    Returns:
        tuple: Embedding model and ChromaDB collection.
    """

    print("Loading embedding model...")
    model = SentenceTransformer("BAAI/bge-base-en-v1.5")

    print("Creating embeddings...")
    embeddings = model.encode(chunks).tolist()

    # Persistent ChromaDB
    client = chromadb.PersistentClient(path="chroma_db")

    # Create collection if it doesn't exist
    collection = client.get_or_create_collection(
        name="pdf_knowledge_base"
    )

    # Clear old data
    existing = collection.get()

    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    # Add new documents
    collection.add(
        ids=[str(i) for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings
    )

    print("Knowledge base ready.")

    return model, collection