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

🧠Embedding & Retrieval

  Each assessment is embedded using all-MiniLM-L6-v2
  
  Embeddings are stored in a FAISS IndexFlatL2
  
  Query embeddings are matched using vector similarity
  
  Generic pages are filtered during retrieval

🌐 API Endpoints

  Health Check
    
    GET /health

  Response
    <img width="1778" height="679" alt="image" src="https://github.com/user-attachments/assets/26601092-773f-4e15-a582-19bfa57ff0ca" />

Recommendation Endpoint

      POST /recommend
      
  Request
  
  <img width="1782" height="470" alt="image" src="https://github.com/user-attachments/assets/8a02c100-a1cc-4333-b01e-ec554da8bd3e" />

  Response

  <img width="1775" height="911" alt="image" src="https://github.com/user-attachments/assets/f15464d0-4559-44b9-aefe-bb1d492992ab" />

🖥️Web Interface

-> Simple HTML + JavaScript frontend
  
-> Accepts hiring requirements as input
  
-> Displays recommended assessments in a table
  
-> Uses the /recommend API endpoint

⚙️ Setup Instructions
1️⃣ Install Dependencies

    pip install -r requirements.txt

2️⃣ Scrape SHL Data

    python scraper/scrape_shl.py

3️⃣ Build FAISS Index

    python -c "from backend.recommender import SHLRecommender; SHLRecommender()"

4️⃣ Run API

    uvicorn backend.app:app --reload
    
<img width="1194" height="907" alt="image" src="https://github.com/user-attachments/assets/c412791a-0751-4926-8e36-687e349c1993" />


API available at:

    http://127.0.0.1:8000
    
Swagger UI:

    http://127.0.0.1:8000/docs

  <img width="1871" height="896" alt="image" src="https://github.com/user-attachments/assets/60a5af34-7115-4faf-9f86-a9d89e753633" />


