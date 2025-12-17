# shl-assessment-recommendation-engine
  Research Intern Assignment – SHL AI Team

📌Overview

  This project implements an AI-powered Assessment Recommendation Engine using SHL’s public product catalog.
  Given a natural language hiring requirement (e.g., “Hiring a Java developer with good communication skills”), the system recommends the most relevant SHL individual assessments using semantic search and vector    similarity.
  
  The solution is built as an industry-grade Retrieval-Augmented Generation (RAG) style system, focusing on clean data ingestion, scalable retrieval, and real-time API access.

🚀Key Features

  🔍 Semantic search over SHL assessments
  
  🧠 Transformer-based text embeddings
  
  ⚡ Fast similarity search using FAISS
  
  🌐 Production-ready REST API (FastAPI)
  
  🖥️ Simple web interface for interaction
  
  📊 Evaluation using Recall@10

🏗️System Architecture

  <img width="2910" height="3665" alt="Assessment Recommendation-2025-12-17-092948" src="https://github.com/user-attachments/assets/9d26336b-e05f-4868-ab1d-98f15e947a7a" />
    
----------------------------------------------------------
| Layer        | Technology                              |
| ------------ | --------------------------------------- |
| Backend      | FastAPI                                 |
| Scraping     | requests, BeautifulSoup                 |
| Embeddings   | SentenceTransformers (all-MiniLM-L6-v2) |
| Vector Store | FAISS                                   |
| Frontend     | HTML + JavaScript                       |
| Hosting      | Railway                                 |
| Evaluation   | Recall@10                               |
----------------------------------------------------------

📁 Project Structure

    shl-assessment-rag/
    │
    ├── scraper/
    │   └── scrape_shl.py          # Scrapes SHL assessment data
    │
    ├── data/
    │   ├── raw_assessments.json   # Cleaned assessment data
    │   └── embeddings.faiss       # FAISS vector index
    │
    ├── backend/
    │   ├── app.py                 # FastAPI application
    │   ├── recommender.py         # RAG logic
    │   └── schema.py              # API request/response models
    │
    ├── evaluation/
    │   └── recall.py              # Recall@10 evaluation
    │
    ├── frontend/
    │   └── index.html             # Web UI
    │
    ├── requirements.txt
    └── README.md

🔍Data Collection
    Scraped SHL’s public product catalog and individual assessment pages
    Removed category-level and generic marketing pages
    Final dataset contains ~278+ individual assessments with:
      Assessment name
      Description
      Product URL
