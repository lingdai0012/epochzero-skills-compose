"""Vector database abstraction layer.

Classes to implement:
    - VectorStore (ABC):
        Abstract interface for vector database operations.

        Methods:
            - async upsert(id: str, vector: List[float], metadata: dict) -> None
            - async search(vector: List[float], filter: Optional[dict], limit: int) -> List[ScoredResult]
            - async delete(ids: List[str]) -> None
            - async count() -> int

    - QdrantStore(VectorStore):
        Qdrant implementation (self-hosted or cloud).

    - PineconeStore(VectorStore):
        Pinecone implementation (managed).
"""
