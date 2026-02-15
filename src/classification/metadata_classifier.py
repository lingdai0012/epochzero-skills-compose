"""Metadata-based rule classifier (free, instant).

Classes to implement:
    - MetadataClassifier:
        Rule-based classifier that uses document metadata to assign hierarchy.

        __init__(org_chart: OrgChart, taxonomy: TopicTaxonomy)

        Methods:
            - classify(chunk: Chunk) -> Optional[ClassifiedChunk]
                Apply rules in order:
                1. Source path mapping (URL/path → department/team)
                2. Access level heuristic (all_company → corporate)
                3. Author's org position (lookup in org_chart)
                4. Keyword matching against taxonomy seed_keywords

                Returns ClassifiedChunk if confidence >= 0.8, else None (fall through to LLM)
"""
