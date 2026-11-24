import numpy as np


def cosine_similarity(query, documents):
    """Cosine similarity between a query vector and each document vector."""
    result = []
    for doc in documents:
        if not np.any(doc) or not np.any(query):
            result.append(0)
            continue
        result.append( (query @ doc) / (np.linalg.norm(query) * np.linalg.norm(doc)) )
    return np.array(result)
