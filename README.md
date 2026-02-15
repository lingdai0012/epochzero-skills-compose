# Auto Skill Generator

Automated SKILL.md generation from corporate documents across Corporate → Department → Team hierarchy.

## Project Structure

```
src/
├── common/           # Shared models, config loaders, utilities
├── connectors/       # Data source connectors (Confluence, GDrive, GitHub, etc.)
├── ingestion/        # Document preprocessing and semantic chunking
├── embedding/        # Vectorization pipeline and vector store
├── classification/   # Hierarchy classification (metadata rules + LLM)
├── generation/       # Skill writing engine (aggregation → planning → generation)
├── qa/               # Quality assurance (structural, content, security)
├── registry/         # Skill storage, versioning, changelog
├── updates/          # Incremental change detection and regeneration
├── api/              # FastAPI REST API and review dashboard
├── agents/           # Agent integration, usage tracking, feedback
└── cli/              # Command-line interface

prompts/              # LLM prompt templates
config/               # YAML configuration files
skills/               # Output: generated SKILL.md files
tests/                # Unit and integration tests
scripts/              # Utility scripts
infra/                # Docker, CI/CD
docs/                 # Documentation
```

## Setup

Requires Python 3.11+.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

```bash
auto-skill-gen run --input ./documents/ --org-chart ./config/org_chart.yaml --taxonomy ./config/topic_taxonomy.yaml --output ./skills/
```
