"""Skill plan review generator for human approval.

Classes to implement:
    - SkillPlanReview:
        Generates a human-readable Markdown table of all planned skills for approval.

        Methods:
            - generate_review(skill_tree: SkillTree) -> str
                Output a Markdown table:
                | Level | Dept | Team | Skill Name | Sources | Est. Lines | Priority |
                Plus: proposed new topics (not in taxonomy), unclassified chunks summary
"""
