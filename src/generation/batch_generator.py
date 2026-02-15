"""Batch generator for parallel skill generation respecting hierarchy order.

Classes to implement:
    - BatchGenerator:
        Orchestrates parallel generation across hierarchy levels.

        Methods:
            - async generate_all(approved_plan: SkillPlan) -> List[GeneratedSkill]
                Phase A: Generate all Corporate skills (no dependencies) — parallel
                Phase B: Generate Department skills (depends on Corporate) — parallel per dept
                Phase C: Generate Team skills (depends on Corporate + Department) — parallel per team

                Each phase waits for the previous to complete so parent summaries are available.
"""
