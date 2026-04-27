import faiss
import numpy as np
import os
import pickle


class VectorStore:
    def __init__(self, dimension=384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

    def add(self, vectors, texts):
        vectors = np.array(vectors).astype("float32")
        self.index.add(vectors)
        self.texts.extend(texts)

    def search(self, query_vector, top_k=1):
        query_vector = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for i in indices[0]:
            if i < len(self.texts):
                results.append(self.texts[i])

        return results

    def save(self):
        os.makedirs("storage", exist_ok=True)
        faiss.write_index(self.index, "storage/faiss.index")

        with open("storage/texts.pkl", "wb") as f:
            pickle.dump(self.texts, f)

    def load(self):
        if os.path.exists("storage/faiss.index"):
            self.index = faiss.read_index("storage/faiss.index")

        if os.path.exists("storage/texts.pkl"):
            with open("storage/texts.pkl", "rb") as f:
                self.texts = pickle.load(f)