"""Knowledge gap detection.

Classes to implement:
    - GapDetector:
        Identifies queries where no skill was triggered but should have been.

        Methods:
            - async detect_gaps(query: str, triggered_skills: List[str]) -> Optional[Gap]
                Use LLM to check:
                - Was there a skill that SHOULD have been triggered but wasn't?
                - Is there a knowledge gap — a topic this query needs that no skill covers?
                Return Gap with suggested_skill if gap detected
"""
