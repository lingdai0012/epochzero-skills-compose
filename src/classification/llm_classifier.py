"""LLM-based content classifier using Claude Haiku.

Classes to implement:
    - LLMContentClassifier:
        Uses LLM to classify chunks that metadata rules couldn't handle.

        __init__(llm_client, org_chart: OrgChart, taxonomy: TopicTaxonomy)

        Methods:
            - async classify(chunk: Chunk) -> ClassifiedChunk
                Build prompt with org chart + taxonomy + chunk content
                Return structured classification with reasoning

            - async batch_classify(chunks: List[Chunk]) -> List[ClassifiedChunk]
                Process in batches of 5-10 chunks per call for cost efficiency
                Uses Claude Haiku (cheaper, fast enough for classification)
"""
