"""Impact analysis: map document changes to affected skills.

Classes to implement:
    - ImpactAnalyzer:
        Maps changed documents → affected chunks → affected skills.

        Methods:
            - analyze(changes: ChangeReport, registry: SkillRegistry) -> List[ImpactedSkill]
                For each change:
                1. Find all chunks from the changed document
                2. Find all skills that use those chunks
                3. Assess severity (high/medium/low) based on change type and chunk importance
                4. Deduplicate results
"""
