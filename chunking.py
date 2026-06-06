from pypdf import PdfReader


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def chunk_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        chunks.append(chunk)

    return chunks


pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

text = extract_text(pdf_path)

chunks = chunk_text(text)

print(f"Total chunks created: {len(chunks)}\n")

for i, chunk in enumerate(chunks[:5]):
    print(f"Chunk {i+1}:")
    print(chunk)
    print("\n" + "=" * 50 + "\n")
