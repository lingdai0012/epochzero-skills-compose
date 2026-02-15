"""Semantic chunker for splitting documents into meaningful chunks.

Classes to implement:
    - SemanticChunker:
        Splits Markdown documents into chunks based on heading structure.

        __init__(max_chunk_tokens: int = 1500, min_chunk_tokens: int = 100)

        Methods:
            - chunk(document: RawDocument) -> List[Chunk]
                Main entry point. Pipeline:
                1. Parse Markdown heading structure
                2. Split by headings into sections
                3. Sub-split large sections by paragraphs
                4. Merge small chunks with siblings
                5. Assign parent-child hierarchy relationships
                6. Compute heading_path breadcrumbs

            - _split_by_headings(content: str) -> List[Section]
            - _split_by_paragraphs(section: Section) -> List[Chunk]
            - _merge_small_chunks(chunks: List[Chunk]) -> List[Chunk]
            - _assign_hierarchy(chunks: List[Chunk]) -> None
"""
