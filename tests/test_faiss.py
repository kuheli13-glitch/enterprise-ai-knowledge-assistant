from app.adapters.embedding_adapter import EmbeddingAdapter
from app.adapters.vector_store import VectorStore

embedder = EmbeddingAdapter()
store = VectorStore()

texts = [
    "Employees are allowed 12 casual leaves per year.",
    "Work from home is allowed 2 days per week."
]

vectors = embedder.encode(texts)
store.add(vectors, texts)

query = "Can I work remotely?"
query_vector = embedder.encode([query])[0]

results = store.search(query_vector)

print(results)
