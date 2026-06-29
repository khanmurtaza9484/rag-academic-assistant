from src.pdf_loader import extract_text

pdf_path = "/home/murtaza-khan/Desktop/Taza/ku/AI/AI_Module_1.pdf"

text = extract_text(pdf_path)

print("PDF loaded successfully!\n")
print(text[:1000])