import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.Client()
collection = client.get_or_create_collection("osmigo_memory")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def embed_and_store(prompt: str, metadata: dict = {}):
    embedding = embedder.encode(prompt).tolist()
    collection.add(
        documents=[prompt],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[str(hash(prompt))]  # or use uuid
    )

def query_memory(query: str, top_k=3):
    query_embedding = embedder.encode(query).tolist()
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results
