from document_loaders import load_pdf


def main():
    documents = load_pdf("sample.pdf")
    print(f"Loaded {len(documents)} documents from the PDF.")
    print("Document content:")
    for i, doc in enumerate(documents):
        print(f"Document {i + 1}:")
        print(doc.page_content)
        print("-" * 40)


if __name__ == "__main__":
    main()
