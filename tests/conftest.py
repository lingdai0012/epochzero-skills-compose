"""Shared test fixtures.

Fixtures to implement:
    - sample_raw_document: RawDocument with sample content and metadata
    - sample_chunks: List of Chunk objects from sample document
    - sample_classified_chunks: List of ClassifiedChunk objects
    - sample_org_chart: OrgChart loaded from tests/fixtures/sample_org_chart.yaml
    - sample_taxonomy: TopicTaxonomy loaded from tests/fixtures/sample_taxonomy.yaml
    - mock_llm_client: Mock LLM client that returns deterministic responses
    - sample_generated_skill: GeneratedSkill with sample SKILL.md content
    - tmp_skills_dir: Temporary directory for skill output
"""
