# Lawyer AI Assistant

Small prototype: PDFs -> PII scrub -> chunk -> embed (nomic-embed-text) -> Chroma vector DB -> retrieve -> LLM (Ollama). Answers cite source PDFs.


This project is split into two possible solutions- a local solution and a cloud solution.

Lawyers documents are sourced from the following dataset:
Contract Understanding Atticus Dataset (CUAD): https://www.atticusprojectai.org/cuad


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

## Notes
- Shows sources for explainability
- Basic PII masking (emails/phones/SSNs)
- Demo only; production would add auth, networking, monitoring
