from src.pdf_loader import extract_text
from src.chunker import create_chunks

pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

text = extract_text(pdf_path)

chunks = create_chunks(text)

print(f"Total chunks: {len(chunks)}")
print()
print(chunks[0])