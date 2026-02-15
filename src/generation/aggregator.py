"""Knowledge aggregator for grouping classified chunks into topics.

Classes to implement:
    - KnowledgeAggregator:
        Groups classified chunks by taxonomy category and identifies sub-topics.

        Methods:
            - async aggregate(chunks: List[ClassifiedChunk], taxonomy: TopicTaxonomy, level: str) -> List[KnowledgeTopic]
                1. Group chunks by taxonomy category
                2. For each group, use LLM to identify sub-topics
                3. Map to existing taxonomy nodes or propose new ones
                4. Return list of KnowledgeTopic with chunk assignments
"""
