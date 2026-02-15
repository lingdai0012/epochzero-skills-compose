"""Skill registry for storing and querying generated skills.

Classes to implement:
    - SkillRegistry:
        Central registry for all generated skills.

        Methods:
            - get(level: str, department?: str, team?: str, status?: str) -> List[GeneratedSkill]
                Query skills by hierarchy level, department, team, and status

            - find_skills_using_chunk(chunk_id: str) -> List[GeneratedSkill]
                Find all skills that reference a given chunk

            - find_dependents(skill_name: str) -> List[str]
                Find all skills that depend_on a given skill

            - publish(skill: GeneratedSkill) -> None
                Mark a skill as published and update registry

            - queue_for_review(skill: GeneratedSkill, qa_result: QAReport) -> None
                Add skill to review queue

            - list_metadata() -> List[dict]
                Return frontmatter metadata for all published skills
"""
