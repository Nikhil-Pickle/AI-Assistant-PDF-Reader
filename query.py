import requests, chromadb
from chromadb.config import Settings

LLM_MODEL = "llama3.1:8b"
EMBED_MODEL = "nomic-embed-text"

def embed_query(q):
    r = requests.post("http://localhost:11434/api/embeddings",
                      json={"model": EMBED_MODEL, "prompt": q})
    r.raise_for_status()
    return r.json()["embedding"]

def ask_llm(prompt):
    r = requests.post("http://localhost:11434/api/generate",
                      json={"model": LLM_MODEL, "prompt": prompt, "stream": False})
    r.raise_for_status()
    return r.json()["response"]

def build_prompt(question, contexts):
    ctx = "\n\n---\n\n".join(contexts)
    return f"""You are a helpful assistant that answers using the provided context.
If the answer isn't in the context, say you don't know.

Question: {question}

Context:
{ctx}

Answer:"""

if __name__ == "__main__":
    db = chromadb.Client(Settings(persist_directory="./store", is_persistent=True))
    col = db.get_collection("legal_docs")

    while True:
        q = input("\nAsk a question (or 'exit'): ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        q_emb = embed_query(q)
        res = col.query(query_embeddings=[q_emb], n_results=5)
        contexts = res["documents"][0] if res["documents"] else []
        prompt = build_prompt(q, contexts)
        ans = ask_llm(prompt)
        print("\n--- Answer ---\n")
        print(ans)
