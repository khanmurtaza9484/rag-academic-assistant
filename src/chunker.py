def create_chunks(text, chunk_size=800, overlap=200):
    """
    Splits the extracted text into overlapping chunks.

    Args:
        text (str): Extracted PDF text.
        chunk_size (int): Maximum size of each chunk.
        overlap (int): Number of overlapping characters between chunks.

    Returns:
        list: List of text chunks.
    """

    chunks = []
    step = chunk_size - overlap

    for i in range(0, len(text), step):
        chunk = text[i:i + chunk_size]

        if chunk:
            chunks.append(chunk)

    return chunks