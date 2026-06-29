def create_chunks(text, chunk_size=800):
    """
    Splits the extracted text into smaller chunks.

    Args:
        text (str): Extracted PDF text.
        chunk_size (int): Maximum size of each chunk.

    Returns:
        list: List of text chunks.
    """

    # Split the text into fixed-size chunks
    chunks = [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]

    # Return the list of chunks
    return chunks