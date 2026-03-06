from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from .models import Smoothie

model = SentenceTransformer('all-MiniLM-L6-v2')


def get_smoothie_embeddings():
    smoothies = Smoothie.objects.all()

    texts = []
    for s in smoothies:
        ingredients = ", ".join([i.name for i in s.ingredients.all()])
        texts.append(ingredients)

    embeddings = model.encode(texts)

    return list(smoothies), embeddings


def recommend_smoothies(user_input, top_k=3):
    smoothies, embeddings = get_smoothie_embeddings()

    user_embedding = model.encode([user_input])

    similarity_scores = cosine_similarity(user_embedding, embeddings)[0]

    top_indices = np.argsort(similarity_scores)[::-1][:top_k]

    return [smoothies[int(i)] for i in top_indices]