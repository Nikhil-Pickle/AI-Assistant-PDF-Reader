# AI Assistant PDF Reader

A lightweight **LLM + RAG prototype** for answering questions about PDF documents.

The demo uses legal agreements (from the [CUAD dataset](https://www.atticusprojectai.org/cuad)) as an example use case, but the pipeline works for any PDF collection.

To keep scope limited, this version only:

* Processes **PDFs** (not yet .txt, .html, etc.)
* Performs basic **PII scrubbing** (emails, phone numbers, SSNs)
* Runs entirely **locally** using [Ollama](https://ollama.ai) for privacy

---

## How It Works

1. **Ingest:** PDFs → scrub PII → chunk text → embed with `nomic-embed-text`
2. **Store:** Save embeddings + metadata into a Chroma vector database
3. **Query:** Retrieve top matches → feed into Ollama LLM → generate grounded answers (with citations)

---

## Local Model Solution

### Prerequisites

* [Ollama](https://ollama.ai) installed and running
* Python 3.9+
* Your PDFs placed inside the `docs/` folder

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

---


## Azure Cloud Solution

## Azure Mapping
- Storage: Azure Data Lake
- Orchestration: Data Factory / Databricks
- Transform/PII: Databricks (bronze/silver/gold)
- Retrieval: Azure Cognitive Search (vectors)
- LLM: Azure OpenAI Service
- Governance/Secrets: Purview / Key Vault


## Limitations
- Chunked retrieval may return partial long sections.
- Basic PII masking (emails/phones/SSNs) only.
- Local, single-user prototype; no auth/monitoring.
- Uses a small local LLM (Ollama); quality < large cloud models.
- Re-run `ingest.py` to refresh the index.

## Azure Mapping (for production)
Data Lake (storage) • Data Factory/Databricks (ETL/PII) • Cognitive Search (vectors) • Azure OpenAI (LLM) • Purview/Key Vault (governance/secrets).


## Notes
- Shows sources for explainability
- Basic PII masking (emails/phones/SSNs)
- Demo only; production would add auth, networking, monitoring
