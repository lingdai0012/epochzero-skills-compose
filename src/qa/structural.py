"""Structural quality checks for generated skills.

Classes to implement:
    - StructuralQA:
        Rule-based structural validation (no LLM needed).

        Methods:
            - check(skill: GeneratedSkill) -> List[QACheck]
                Runs all structural checks:
                - check_frontmatter_valid: Valid YAML frontmatter
                - check_required_fields: name, description, level present
                - check_line_count: Under 500 lines
                - check_heading_structure: H1 → H2 → H3 ordered
                - check_no_empty_sections: No headings with no content
                - check_depends_on_valid: Referenced skills exist in registry
"""
