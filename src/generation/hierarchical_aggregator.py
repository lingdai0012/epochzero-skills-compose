"""Hierarchical aggregator for top-down Corporate → Department → Team generation.

Classes to implement:
    - HierarchicalAggregator:
        Top-down aggregation with deduplication against parent levels.

        Methods:
            - async aggregate_all(classified_chunks: List[ClassifiedChunk]) -> SkillTree
                Step 1: Corporate level — filter + cluster + plan
                Step 2: Department level (per dept) — filter + dedup against corporate + cluster + plan
                Step 3: Team level (per team) — filter + dedup against corporate+dept + cluster + plan

            - _filter(chunks, level, department?, team?) -> List[ClassifiedChunk]
            - async _dedup_against(chunks, parent_skills) -> List[ClassifiedChunk]
            - async _cluster(chunks) -> List[KnowledgeTopic]
            - async _plan_skills(topics, parent_context) -> List[PlannedSkill]
"""
