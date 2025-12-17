from pydantic import BaseModel
from typing import List


class RecommendRequest(BaseModel):
    query: str
    top_k: int = 5


class Assessment(BaseModel):
    assessment_name: str
    assessment_url: str


class RecommendResponse(BaseModel):
    query: str
    recommendations: List[Assessment]
