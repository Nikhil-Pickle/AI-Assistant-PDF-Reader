# AI Assistant PDF Reader

A lightweight **LLM + RAG prototype** for answering questions about PDF documents.

The demo uses legal agreements (from the [CUAD dataset](https://www.atticusprojectai.org/cuad)) as an example use case, but the pipeline works for any PDF collection.

---

## 🔍 How It Works

1. **Ingest** – PDFs → scrub PII → chunk text → embed with `nomic-embed-text`
2. **Store** – Save embeddings + metadata into a **Chroma** vector database
3. **Query** – Retrieve top matches → feed into **Ollama LLM** → generate grounded answers (with citations)

In other words- drop PDF files in the "docs" folder, run ingest.py, run query.py.

📌 **Visual Overview**

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

In my example, I use all the PDFS found in CUAD_v1.zip\CUAD_v1\full_contract_pdf\Part_I\License_Agreements :

![example powershell output](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-26%20192915.png)

### 👏 **Congratulations!** You now have a fully functional PDF AI Assistant!

---

## ☁️ Azure Cloud (Alternative Solution)


This shows how to deploy a similar RAG flow but using the Azure ecosystem, using only **Blob Storage** + **Azure AI Search**.
No Databricks/Data Factory were used here — just direct indexing.

---

### 🔹 Step 1 — Create a Storage Account + Container

1. In Azure Portal, create a **Storage Account** (ADLS Gen2).
2. Create a **Container** (e.g., `docs`).
3. Set **access level = Private** (secure by default).
4. Upload your PDFs into this container.

![screenshot placeholder — storage container with PDFs](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-27%20111519.png)

---

### 🔹 Step 2 — Create an Azure AI Search Service

1. In Portal, search for **Azure AI Search** → **Create**.
2. Use the **Free (F)** tier (limit 3 indexes).
3. Wait for deployment to complete.

![screenshot placeholder — AI Search service overview](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-27%20111939.png)

---

### 🔹 Step 3 — Index Your Documents

1. Open your AI Search resource → **Import data**.
2. Choose **Azure Blob Storage** → point to your container.
3. Add a **connection string** to authenticate.
4. Select **Content extraction** = *Default text*.
5. Create:

   * **Data source**: your blob container
   * **Index**: choose key field = `metadata_storage_path`, content field = `content`, title/source = `metadata_storage_name`
   * **Indexer**: name it (e.g., `pdf-indexer`)

---

### 🔹 Step 4 — Run the Indexer

1. Run the indexer manually the first time.
2. It extracts text from PDFs and populates your **search index**.
3. Verify success under **Indexers → Execution history**.

![screenshot placeholder — successful indexer run](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-27%20112334.png)

---

### 🔹 Step 5 — Query Your Data

You now have a search-ready index.

**Option A — No-code:**

* Use **Search Explorer** inside the Azure Portal.
* Try queries like:

  * `confidentiality`
  * `"termination clause"`

![screenshot placeholder — Search Explorer results](https://raw.githubusercontent.com/Nikhil-Pickle/AI-Assistant-PDF-Reader/refs/heads/main/Screenshot%202025-08-27%20112658.png)


---

### 🔹 Step 6 — (Optional) Connect to Azure OpenAI

On the Free tier, “Bring Your Own Data” isn’t available.
But in production you’d:

* Deploy an **Azure OpenAI model**
* Add a **data connection to AI Search**
* Chat directly with your contracts (with citations).

---

### ✅ What This Achieves

* **Storage** in Blob (secure, private) or Azure Data Lake
* **Indexing + retrieval** with Azure AI Search
* Lawyers (or apps) can now query thousands of contracts with keyword or semantic search
* Future-ready for **Azure OpenAI** integration

---

## ⚠️ Limitations

* Basic PII masking (emails/phones/SSNs) only.
* Local, single-user prototype → no auth/monitoring.
* Uses a small local LLM (Ollama); quality < larger cloud models.
* Free Azure tier limits: full vector + “Bring your own data” integration requires Basic+.

---

## ✅ Notes

* Built as a **demo prototype**; production would add auth, monitoring, networking, and scaling.
* Can be extended to more formats (.txt, .html, .docx).

---


## 🚀 Next Steps

* Swap Ollama → Azure OpenAI for full-cloud solution
* Enable vector + semantic ranker in Azure AI Search
* Add simple web front-end (Streamlit or Flask) for user-friendly UI

---
