"""Embedding pipeline for batch vectorization and retrieval.

Classes to implement:
    - EmbeddingPipeline:
        Manages batch embedding and metadata-filtered retrieval.

        __init__(model: str = "voyage-3", vector_store: VectorStore)

        Methods:
            - async index_chunks(chunks: List[Chunk]) -> None
                Batch embed chunks (max 128 per API call for Voyage)
                Upsert with rich metadata for filtering:
                    document_id, department, team, content_type,
                    access_level, updated_at, heading_path

            - async retrieve(query: str, filters: Optional[dict], top_k: int = 20) -> List[ScoredChunk]
                Embed query, search with metadata filters, return scored results

            - async delete_by_document(document_id: str) -> None
                Remove all vectors for a document (for re-indexing)
"""
