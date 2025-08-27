# AI Assistant PDF Reader

A lightweight **LLM + RAG prototype** for answering questions about PDF documents.

The demo uses legal agreements (from the [CUAD dataset](https://www.atticusprojectai.org/cuad)) as an example use case, but the pipeline works for any PDF collection.

---

## 🔍 How It Works

1. **Ingest** – PDFs → scrub PII → chunk text → embed with `nomic-embed-text`
2. **Store** – Save embeddings + metadata into a **Chroma** vector database
3. **Query** – Retrieve top matches → feed into **Ollama LLM** → generate grounded answers (with citations)

In other words- drop PDF files in the "docs" folder, run ingest.py, run query.py.
You now have a fully functional AI assistant for your PDFs.


📌 **Visual Overview**
*(replace with diagram later — e.g., draw\.io export)*

![steps to use](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/image.png)

---

## 💻 Local Model Solution

Run everything locally for free & private experimentation.

### Prerequisites

* [Ollama](https://ollama.ai) installed and running
* Python 3.9+
* PDFs placed inside the `docs/` folder

### Setup & Run

```bash
# Pull models
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# Install dependencies
pip install pypdf chromadb requests

# Ingest PDFs into the vector store
python ingest.py

# Ask questions against your documents
python query.py
```

📸 **Example run:**

![example powershell output](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-26%20192915.png)

---

## ☁️ Azure Cloud (Alternative Solution)

An enterprise-ready path using **Azure AI ecosystem** instead of local tools.

### Azure Mapping

* **Storage**: Azure Data Lake
* **Orchestration**: Data Factory / Databricks
* **Transform + PII**: Databricks (bronze/silver/gold)
* **Retrieval**: Azure AI Search (formerly Cognitive Search)
* **LLM**: Azure OpenAI Service
* **Governance & Security**: Purview / Key Vault

📌 **Architecture Diagram**
*(replace with diagram of Azure services mapped to flow)*

![azure-architecture-placeholder](https://via.placeholder.com/800x400.png?text=Azure+Architecture+Placeholder)

---

## ⚠️ Limitations

* Chunked retrieval may return partial long sections.
* Basic PII masking (emails/phones/SSNs) only.
* Local, single-user prototype → no auth/monitoring.
* Uses a small local LLM (Ollama); quality < larger cloud models.
* Free Azure tier limits: full vector + “Bring your own data” integration requires Basic+.

---

## ✅ Notes

* Sources shown for explainability.
* Built as a **demo prototype**; production would add auth, monitoring, networking, and scaling.
* Can be extended to more formats (.txt, .html, .docx).

---


## 🚀 Next Steps

* Swap Ollama → Azure OpenAI for full-cloud solution
* Enable vector + semantic ranker in Azure AI Search
* Add simple web front-end (Streamlit or Flask) for user-friendly UI

---
