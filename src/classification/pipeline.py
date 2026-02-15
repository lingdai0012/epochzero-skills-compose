"""Combined hierarchy classification pipeline.

Classes to implement:
    - HierarchyClassifier:
        Two-stage classifier: metadata rules first, LLM fallback for uncertain cases.

        __init__(metadata_classifier: MetadataClassifier, llm_classifier: LLMContentClassifier)

        Methods:
            - async classify(chunk: Chunk) -> ClassifiedChunk
                1. Try metadata rules (free, instant)
                2. If confidence >= 0.8, return result
                3. Fall back to LLM analysis
                4. If LLM confidence < 0.7, flag needs_review = True

            - async classify_batch(chunks: List[Chunk]) -> List[ClassifiedChunk]
                Classify a batch: metadata rules first, collect LLM-needed chunks,
                batch-classify via LLM
"""
