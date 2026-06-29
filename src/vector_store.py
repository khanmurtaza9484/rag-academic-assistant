# Import required libraries
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


def create_vector_store(chunks):
    """
    Creates embeddings for text chunks and stores them
    in a FAISS vector index.

    Args:
        chunks (list): List of text chunks.

    Returns:
        tuple: Embedding model and FAISS index.
    """

    # Load the sentence transformer model
    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings for all text chunks
    print("Creating embeddings...")
    embeddings = model.encode(chunks)

    # Convert embeddings to float32 (required by FAISS)
    embeddings = np.array(embeddings).astype("float32")

    # Get the embedding dimension
    dimension = embeddings.shape[1]

    # Create a FAISS index
    index = faiss.IndexFlatL2(dimension)

    # Add embeddings to the FAISS index
    index.add(embeddings)

    print("Knowledge base ready.")

    # Return the model and FAISS index
    return model, index