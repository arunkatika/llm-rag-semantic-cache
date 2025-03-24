# 🧠 LLM RAG (Retrieval-Augmented Generation) App with Semantic Caching

A fully **offline**, **privacy-first** Retrieval-Augmented Generation (RAG) application that allows users to upload **PDFs** and query them using **LLMs (LLaMA 3.2B)** with **semantic caching** and **Re-ranking** — all running **locally** on your machine.

> 🔐 No cloud. No API keys. 100% local inference & vector search.

---
![Thumbnail](https://github.com/user-attachments/assets/0af67786-9871-4fcb-84ba-513f9899ab9c)

## 📌 Features

- 🔍 Document Q&A using semantic search over uploaded PDFs
- 🧠 LLM Integration with [Ollama](https://ollama.com) (LLaMA 3.2B)
- 🧭 Vector indexing and chunking using **ChromaDB**
- 🧠 Semantic Caching with **Redis** to avoid redundant queries
- 🪄 Re-ranking using **CrossEncoder (MS MARCO)**
- 💡 Clean UI built with **Streamlit**
- 📦 Fully local architecture (no external API calls)

---

## ⚙️ Tech Stack

| Tool                | Role                                  |
|---------------------|----------------------------------------|
| 🦙 Ollama            | Local LLM & Embedding model serving    |
| 🧠 LLaMA 3.2B         | Large Language Model via Ollama        |
| 📚 Nomic Embed Text  | Embedding model for vector search      |
| 📦 ChromaDB          | Vector store for document chunks       |
| 🔁 Redis + LangChain | Semantic cache storage & retrieval     |
| 📊 CrossEncoder      | Re-ranking of retrieved results        |
| 📄 Streamlit         | UI for document upload and Q&A         |

---

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/arunkatika/llm-rag-semantic-cache.git
cd llm-rag-semantic-cache
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Pull the models using Ollama
```bash
ollama pull llama3:3b
ollama pull nomic-embed-text
```

### 4. Run Redis using Docker
```bash
docker run -d -p 6379:6379 --name redis redis/redis-stack:latest
```

### 5. Start the app
```bash
streamlit run app.py
```

---

## 📁 How It Works

1. **Upload PDF** → Document is chunked and embedded → Stored in **ChromaDB**
2. **Ask a question**:
   - First checks **Redis cache** for semantic match
   - If **match found**: returns cached answer instantly ⚡
   - If **no match**: 
     - Queries vector store
     - Re-ranks with CrossEncoder
     - Passes top results to LLaMA 3.2B
     - Caches the new Q&A pair in Redis

---

## 🧪 Use Cases

- Internal document search assistant
- Study notes summarizer
- Legal/compliance document QA
- Resume & job document chatbot
- Enterprise knowledge Q&A system

---

## 🛠 Example: CSV Format for Semantic Cache

```csv
question,answer
"What is the target candidate description?","The AWS Certified AI Practitioner is intended for..."
"What is AWS Certified AI Practitioner?","It validates foundational knowledge of AI/ML services on AWS..."
```

📂 Upload this using **Cache mode** in the app.

---

## 🧠 Tips

- Use meaningful filenames — they become embedding IDs
- Monitor Redis & Chroma for performance/debugging
- Tune semantic cache threshold for match sensitivity

---

## 🔧 Development Notes

### 📦 Install core dependencies
```bash
pip install ollama chromadb sentence-transformers streamlit pymupdf langchain-community
```

### 📦 For semantic cache support
```bash
pip install langchain-ollama==0.2.2 langchain-redis==0.2.0
```

### 🐳 Redis via Docker
```bash
docker run -d -p 6379:6379 redis/redis-stack:latest
```

### 🧪 Redis Cache Debugging
```bash
docker exec -it redis bash
redis-cli
KEYS *
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---
