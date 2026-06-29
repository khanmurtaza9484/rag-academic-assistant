from src.pdf_loader import extract_text
from src.chunker import create_chunks
from src.vector_store import create_vector_store

# Path to the PDF
pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

# Extract text from the PDF
text = extract_text(pdf_path)

# Split text into chunks
chunks = create_chunks(text)

# Create the vector store
model, index = create_vector_store(chunks)

print("\nFAISS index created successfully!")
print(f"Total vectors stored: {index.ntotal}")