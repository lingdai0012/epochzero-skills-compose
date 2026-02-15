"""Skill file writer for persisting generated skills to disk.

Classes to implement:
    - SkillFileWriter:
        Writes generated skills to the correct directory structure on disk.

        Methods:
            - write_to_disk(skill: GeneratedSkill, base_dir: str) -> str
                Determine path: skills/{level}/{dept?}/{team?}/{skill_name}/SKILL.md
                Write SKILL.md
                Write reference files to references/ subdirectory if any
                Return the written path

            - write_registry(skills: List[GeneratedSkill], base_dir: str) -> None
                Generate registry.json with all skill metadata for quick lookups
"""
