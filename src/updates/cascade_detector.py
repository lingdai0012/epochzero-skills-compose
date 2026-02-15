"""Cascade update detection for dependent skills.

Classes to implement:
    - CascadeDetector:
        When a parent skill changes, checks if dependent skills need updating too.

        Methods:
            - detect(updated_skill: GeneratedSkill, registry: SkillRegistry) -> List[str]
                Find all skills that depend_on the updated skill
                For each dependent, check if the change affects referenced content
                Return list of skill names that need re-evaluation
"""
