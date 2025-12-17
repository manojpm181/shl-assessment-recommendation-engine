import json
import os
import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
FAISS_PATH = "data/embeddings.faiss"

class SHLRecommender:
    def __init__(self, data_path="data/raw_assessments.json"):
        self.model = SentenceTransformer(MODEL_NAME)

        with open(data_path, "r", encoding="utf-8") as f:
            self.assessments = json.load(f)

        self.texts = [
            a["name"] + " " + a["description"]
            for a in self.assessments
        ]

        try:
            if os.path.exists(FAISS_PATH):
                print("Loading existing FAISS index...")
                self.index = faiss.read_index(FAISS_PATH)
            else:
                raise RuntimeError("FAISS file not found")

        except Exception as e:
            print("FAISS load failed, rebuilding index...")
            embeddings = self.model.encode(
                self.texts,
                convert_to_numpy=True,
                show_progress_bar=True
            )

            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)
            self.index.add(embeddings)

            faiss.write_index(self.index, FAISS_PATH)
            print("FAISS index rebuilt and saved")

    def recommend(self, query, top_k=10):
        q_emb = self.model.encode([query], convert_to_numpy=True)
        _, indices = self.index.search(q_emb, top_k * 2)

        results = []
        for idx in indices[0]:
            item = self.assessments[idx]

            if item["url"].count("/") <= 5:
                continue

            results.append({
                "assessment_name": item["name"],
                "assessment_url": item["url"]
            })

            if len(results) == top_k:
                break

        return results
