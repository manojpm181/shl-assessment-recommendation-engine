import sys
import os
import json

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.recommender import SHLRecommender


def recall_at_k(recommender, test_queries, ground_truth, k=5):
    hits = 0
    total = len(test_queries)

    for query, true_items in zip(test_queries, ground_truth):
        results = recommender.recommend(query, top_k=k)
        predicted_names = [r["assessment_name"] for r in results]

        if any(
            any(gt.lower() in name.lower() for name in predicted_names)
            for gt in true_items
        ):
            hits += 1

    return hits / total


if __name__ == "__main__":
    rec = SHLRecommender()

    test_queries = [
        "Java developer hiring",
        "Leadership assessment",
        "Communication skills test",
        "Coding skills evaluation",
        "Personality assessment"
    ]

    ground_truth = [
        ["java", "coding"],
        ["leadership"],
        ["communication", "language"],
        ["coding"],
        ["personality"]
    ]

    score = recall_at_k(rec, test_queries, ground_truth, k=5)
    print(f"Recall@5: {score:.2f}")
