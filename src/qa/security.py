"""Security quality checks for generated skills.

Classes to implement:
    - SecurityQA:
        Rule-based security validation.

        Methods:
            - check(skill: GeneratedSkill) -> List[QACheck]
                Runs all security checks:
                - check_no_secrets: No API keys, passwords, tokens in content
                - check_no_pii: No personal identifiable information
                - check_access_level: Correct confidentiality classification
"""
