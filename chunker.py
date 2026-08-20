from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_documents(documents, chunk_size=1000, chunk_overlap=200):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    chunks = []
    for document in documents:
        document_chunks = text_splitter.split_text(document.page_content)
        chunks.extend(document_chunks)
    return chunks
