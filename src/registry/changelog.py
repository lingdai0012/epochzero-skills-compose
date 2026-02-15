"""Changelog generation for skill version diffs.

Classes to implement:
    - ChangelogGenerator:
        Uses LLM to generate human-readable changelogs comparing skill versions.

        Methods:
            - async generate(old_skill: str, new_skill: str, change: Change) -> str
                Compare old and new skill versions
                Return 3-5 bullet points describing changes:
                  added content, removed content, changed definitions, updated references
"""
