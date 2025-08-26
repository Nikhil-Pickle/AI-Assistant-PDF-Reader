# Lawyer AI Assistant

Small prototype: PDFs -> PII scrub -> chunk -> embed (nomic-embed-text) -> Chroma vector DB -> retrieve -> LLM (Ollama). Answers cite source PDFs.


This project is split into two possible solutions- a local solution and a cloud solution.

Lawyers documents are sourced from the following dataset:
Contract Understanding Atticus Dataset (CUAD): https://www.atticusprojectai.org/cuad
The CUAD_V1.zip dataset, using PDF files from CUAD_v1.zip\CUAD_v1\full_contract_pdf\Part_I\License_Agreements


## Local Model Solution



## Run
ollama pull llama3.1:8b  
ollama pull nomic-embed-text   
pip install pypdf chromadb requests  
python ingest.py  
python query.py  



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
