from app.adapters.embedding_adapter import EmbeddingAdapter

embedder = EmbeddingAdapter()

vectors = embedder.encode(["Hello world", "Work from home policy"])

print(vectors.shape)
