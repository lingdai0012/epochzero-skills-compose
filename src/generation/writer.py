"""Skill writer for generating SKILL.md content via LLM.

Classes to implement:
    - SkillWriter:
        Composes prompts and generates SKILL.md content using Claude Sonnet.

        SKILL_TEMPLATE: str
            YAML frontmatter template (name, description, level, department,
            team, depends_on, sources, generated_at, version)

        Methods:
            - async write_skill(plan: PlannedSkill, source_chunks: List[Chunk], parent_skills: List[str]) -> GeneratedSkill
                1. Compose prompt with:
                   - Skill plan (name, level, description)
                   - Parent skill summaries (to avoid repetition)
                   - Source chunks (the actual knowledge)
                   - Writing guidelines (imperative tone, <500 lines, etc.)
                2. Call LLM (Claude Sonnet for writing quality)
                3. Post-process: validate YAML frontmatter, check line count
                4. If >500 lines, split into SKILL.md + references/

            - async write_all(plan: SkillPlan, ...) -> SkillRegistry
                Generate top-down: Corporate → Department → Team
                Each level receives parent summaries to enable referencing
"""
