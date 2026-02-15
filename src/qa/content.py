"""Content quality checks using LLM evaluation.

Classes to implement:
    - ContentQA:
        LLM-based content quality checks.

        Methods:
            - async check(skill: GeneratedSkill) -> List[QACheck]
                Runs all content checks:
                - check_accuracy: Consistent with source chunks
                - check_completeness: Covers key topics from plan
                - check_redundancy: Not duplicating parent skill content
                - check_actionability: Instructions are concrete and executable
                - check_trigger_coverage: Description triggers well for expected queries
"""
