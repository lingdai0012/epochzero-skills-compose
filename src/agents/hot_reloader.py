"""Skill hot-reload mechanism for live agents.

Classes to implement:
    - SkillHotReloader:
        Notifies affected agents when a skill is published or updated.

        Methods:
            - async on_skill_published(skill_name: str) -> None
                Find all agents using this skill
                Send reload signal to each
                Log reload events
"""
