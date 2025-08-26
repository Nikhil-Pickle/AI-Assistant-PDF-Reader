import os
import re
import requests
from pypdf import PdfReader
import chromadb
from chromadb.config import Settings

# --- simple PII scrubbing ---
EMAIL = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
PHONE = re.compile(r'(\+?\d{1,2}[\s\-]?)?(\(?\d{3}\)?[\s\-]?)?\d{3}[\s\-]?\d{4}')
SSN = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')

def scrub(t: str) -> str:
    t = EMAIL.sub("[EMAIL]", t)
    t = PHONE.sub("[PHONE]", t)
    t = SSN.sub("[SSN]", t)
    return t

def load_chunks(path, chunk_chars=1200, overlap=200):
    basename = os.path.basename(path)
    reader = PdfReader(path)
    pages = [(p.extract_text() or "") for p in reader.pages]
    text = scrub("\n".join(pages))

    chunks = []
    i = 0
    while i < len(text):
        raw_chunk = text[i:i+chunk_chars]
        i += (chunk_chars - overlap)
        if raw_chunk.strip():
            chunks.append(f"SOURCE_FILE: {basename}\n\n{raw_chunk}")
    return chunks

def embed_batch(texts, model="nomic-embed-text"):
    url = "http://localhost:11434/api/embeddings"
    vecs = []
    for t in texts:
        r = requests.post(url, json={"model": model, "prompt": t})
        r.raise_for_status()
        vecs.append(r.json()["embedding"])
    return vecs

if __name__ == "__main__":
    client = chromadb.Client(Settings(persist_directory="./store", is_persistent=True))
    try:
        client.delete_collection("legal_docs")
    except Exception:
        pass
    col = client.get_or_create_collection("legal_docs")

    pdfs = [os.path.join("docs", f) for f in os.listdir("docs") if f.lower().endswith(".pdf")]
    if not pdfs:
        print("Put some PDFs in ./docs and run again.")
        raise SystemExit(1)

    docs, ids, metas = [], [], []
    for path in pdfs:
        chunks = load_chunks(path)
        base = os.path.basename(path)
        for idx, ch in enumerate(chunks):
            docs.append(ch)
            ids.append(f"{base}__{idx}")
            metas.append({"source": base, "chunk_index": idx})

    print(f"Embedding {len(docs)} chunks...")
    embs = embed_batch(docs)
    col.add(documents=docs, embeddings=embs, ids=ids, metadatas=metas)
    print("Done. Vector store ready in ./store")
