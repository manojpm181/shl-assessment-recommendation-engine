from fastapi.middleware.cors import CORSMiddleware
from backend.schema import RecommendRequest, RecommendResponse

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from backend.recommender import SHLRecommender

app = FastAPI(title="SHL Assessment Recommendation API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


recommender = SHLRecommender()

class RecommendRequest(BaseModel):
    query: str
    top_k: int = 10

class Assessment(BaseModel):
    assessment_name: str
    assessment_url: str

class RecommendResponse(BaseModel):
    query: str
    recommendations: List[Assessment]

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/recommend", response_model=RecommendResponse)
def recommend(req: RecommendRequest):
    results = recommender.recommend(req.query, req.top_k)
    return {
        "query": req.query,
        "recommendations": results
    }

