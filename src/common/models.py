"""Core data models shared across the system.

Classes to implement:
    - RawDocument: Raw ingested document with source, title, content (Markdown), content_type, metadata
    - DocumentMetadata: Author, department, team, timestamps, access_level, tags, org_path, source_url
    - Chunk: Document fragment with heading_path breadcrumb, position, token_count, parent_chunk_id
    - ClassifiedChunk: Chunk + skill_category, hierarchy_level, department, team, confidence, method
    - KnowledgeTopic: Aggregated topic with chunk assignments and taxonomy mapping
    - PlannedSkill: Skill plan with name, level, department, team, source_chunks, depends_on, priority
    - SkillPlan: Collection of planned skills organized by hierarchy level
    - SkillTree: Full tree of corporate/department/team skill plans
    - GeneratedSkill: Generated SKILL.md content + reference files + QA result + version + status
    - QAReport: Quality assurance check results (structural, content, security)
    - QACheck: Individual QA check result (name, passed, score, message)
    - LoadedSkillSet: Skills loaded for an agent (metadata + full content for priority skills)
    - ChangeReport: Detected changes across sources (new, modified, deleted documents)
    - ImpactedSkill: Skill affected by a source change with severity assessment
    - UsageEvent: Agent skill usage event (trigger, load, reference)
    - Gap: Detected knowledge gap (query where no skill triggered but should have)
"""
