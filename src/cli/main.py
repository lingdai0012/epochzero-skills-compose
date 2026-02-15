"""CLI entry point with subcommands.

Subcommands to implement:
    - run: Full pipeline (ingest → classify → plan → generate)
        --input: Document directory or source config
        --org-chart: Path to org_chart.yaml
        --taxonomy: Path to topic_taxonomy.yaml
        --output: Output directory for generated skills

    - ingest: Ingest documents from sources
        --input: Document directory
        --source-config: Path to source_config.yaml

    - classify: Classify ingested chunks
        --chunks-db: Path to chunks data

    - plan: Generate skill plan from classified chunks
        --classified: Path to classified chunks data

    - generate: Generate skills from approved plan
        --plan: Path to approved plan data
        --output: Output directory
"""


def main() -> None:
    """CLI entry point."""
    ...
