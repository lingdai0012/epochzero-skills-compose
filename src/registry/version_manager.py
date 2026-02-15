"""Semantic versioning for generated skills.

Classes to implement:
    - VersionManager:
        Manages semantic versioning for skill updates.

        Methods:
            - bump(current: str, change_type: str) -> str
                Bump version based on change type:
                - "content_update" → patch (e.g., 1.0.0 → 1.0.1)
                - "structural_change" → minor (e.g., 1.0.1 → 1.1.0)
                - "hierarchy_change" → major (e.g., 1.1.0 → 2.0.0)

            - initial_version() -> str
                Returns "1.0.0" for new skills
"""
