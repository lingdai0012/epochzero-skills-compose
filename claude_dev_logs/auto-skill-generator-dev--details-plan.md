# Auto Skill Generator — Development Plan

> **Project**: Automated multi-level SKILL.md generation system from corporate documents
> **Version**: 1.0
> **Date**: 2026-02-15
> **Status**: Planning

---

## Executive Summary

This document outlines the full development plan for the **Auto Skill Generator** — a system that ingests corporate documents across heterogeneous data sources, classifies and organizes knowledge by organizational hierarchy (Corporate → Department → Team), and automatically generates structured SKILL.md files for use by AI Agent systems.

The project is divided into **5 phases** spanning approximately **20-26 weeks**, progressing from a manually-seeded MVP to a fully automated, self-improving pipeline.

---

## Phase Overview

| Phase | Name | Duration | Key Outcome |
|-------|------|----------|-------------|
| Phase 0 | Foundation & Setup | Weeks 1–2 | Dev environment, infrastructure, org chart, topic taxonomy |
| Phase 1 | Manual-Seed MVP | Weeks 3–6 | 5–10 Corporate-level Skills from hand-picked documents |
| Phase 2 | Automated Ingestion & Classification | Weeks 7–12 | Multi-source ingestion, LLM classification, 3-level generation |
| Phase 3 | Incremental Updates & QA | Weeks 13–18 | Change detection, partial regeneration, review dashboard |
| Phase 4 | Agent Integration & Feedback Loop | Weeks 19–22 | Live Agent loading, usage tracking, feedback-driven refinement |
| Phase 5 | Optimization & Scale | Weeks 23–26+ | Cost optimization, multi-language, advanced analytics |

---

## Phase 0: Foundation & Setup (Weeks 1–2)

### 0.1 — Development Environment

**Objective**: Establish all infrastructure and tooling needed for development.

**Tasks**:

- Set up monorepo structure:
  ```
  auto-skill-generator/
  ├── src/
  │   ├── connectors/          # Data source connectors
  │   ├── ingestion/           # Document preprocessing
  │   ├── embedding/           # Vectorization layer
  │   ├── classification/      # Content analysis & hierarchy
  │   ├── generation/          # Skill writing engine
  │   ├── qa/                  # Quality assurance checks
  │   ├── registry/            # Skill storage & distribution
  │   └── common/              # Shared utilities, types, config
  ├── skills/                  # Output: generated Skills
  │   ├── corporate/
  │   ├── departments/
  │   └── teams/
  ├── config/
  │   ├── org_chart.yaml       # Organization structure
  │   ├── topic_taxonomy.yaml  # Seed topic definitions
  │   ├── source_config.yaml   # Data source credentials & settings
  │   └── generation_config.yaml # LLM parameters & templates
  ├── tests/
  ├── scripts/
  ├── docs/
  └── infra/                   # Terraform / Docker / CI
  ```
- Configure Python 3.11+ project with `pyproject.toml`, linting (ruff), typing (mypy), testing (pytest)
- Set up Docker Compose for local development (vector DB, task queue)
- Provision cloud resources: object storage (S3/GCS), vector database, LLM API keys
- Set up CI/CD pipeline (GitHub Actions or equivalent)

**Deliverables**: Working dev environment, CI pipeline, infrastructure-as-code templates

**Estimated Effort**: 1 developer × 1 week

---

### 0.2 — Organization Chart & Topic Taxonomy

**Objective**: Create the two foundational data structures that drive the entire hierarchy system.

**Tasks**:

- Interview stakeholders (department heads, team leads) or extract from HR system
- Build `org_chart.yaml`:
  ```yaml
  company:
    name: "Partners Group"
    departments:
      - name: "Investments"
        head: "Wolf-Henning Scheider"
        teams:
          - name: "PE Technology"
            focus: "Technology sector private equity deals"
            key_tools: ["DealCloud", "FactSet"]
            headcount: 25
          - name: "PE Health & Life"
            focus: "Healthcare and life sciences PE"
            headcount: 20
          - name: "Infrastructure"
            focus: "Infrastructure investments and platform building"
            headcount: 30
          - name: "Real Estate"
            focus: "Real estate acquisitions and development"
            headcount: 22
          - name: "Private Credit"
            focus: "Direct lending, CLOs, credit secondaries"
            headcount: 18
          - name: "Royalties"
            focus: "Music, pharma, and IP royalty streams"
            headcount: 8

      - name: "Client Solutions"
        teams:
          - name: "Institutional EMEA"
            focus: "European institutional client relationships"
          - name: "Institutional Americas"
            focus: "North American institutional clients"
          - name: "Private Wealth"
            focus: "Wealth advisory and evergreen products"
          - name: "Product Structuring"
            focus: "Fund structuring, ELTIF, SICAR"

      - name: "Operations & Technology"
        teams:
          - name: "Platform Engineering"
            focus: "Core infrastructure, APIs, DevOps"
          - name: "Data & Analytics"
            focus: "Data pipelines, reporting, BI"
          - name: "Information Security"
            focus: "Cybersecurity, compliance tooling"

      - name: "Finance & Risk"
        teams:
          - name: "Fund Accounting"
          - name: "Risk Management"
          - name: "Compliance"

      - name: "Human Resources"
        teams:
          - name: "Talent Acquisition"
          - name: "Learning & Development"

      - name: "Legal"
        teams:
          - name: "Transactions"
          - name: "Regulatory"

      - name: "Marketing & Communications"
        teams:
          - name: "Brand & Content"
          - name: "Digital & Events"
          - name: "Investor Relations"
  ```

- Build `topic_taxonomy.yaml` — the seed topic skeleton:
  ```yaml
  corporate:
    brand-identity:
      description: "Visual identity, logo usage, tone of voice, style guide"
      seed_keywords: ["logo", "brand", "color", "font", "tone of voice"]
      expected_sources: ["marketing wiki", "brand handbook", "website"]
      priority: high

    glossary:
      description: "Company-specific and industry terminology definitions"
      seed_keywords: ["glossary", "definition", "terminology", "term"]
      priority: high

    compliance-and-risk:
      description: "Regulatory requirements, risk policies, KYC/AML, GDPR"
      seed_keywords: ["compliance", "regulation", "policy", "FINMA", "SEC"]
      priority: high

    values-and-culture:
      description: "Mission, values, code of conduct, behavioral expectations"
      seed_keywords: ["values", "culture", "mission", "code of conduct"]
      priority: medium

    sustainability-esg:
      description: "ESG framework, exclusion policy, SFDR disclosures, SDG alignment"
      seed_keywords: ["ESG", "sustainability", "SFDR", "exclusion", "SDG"]
      priority: medium

    corporate-governance:
      description: "Board structure, executive team, AGM procedures, shareholder info"
      seed_keywords: ["governance", "board", "AGM", "shareholder"]
      priority: low

  departments:
    investments:
      valuation-methodology:
        description: "Valuation frameworks, DCF, multiples, NAV calculation"
        seed_keywords: ["valuation", "DCF", "multiple", "EBITDA", "NAV"]
        priority: high

      due-diligence:
        description: "DD process, checklists, red flags, third-party coordination"
        seed_keywords: ["due diligence", "DD", "checklist", "assessment"]
        priority: high

      portfolio-monitoring:
        description: "Portfolio company oversight, KPI tracking, reporting cycles"
        seed_keywords: ["monitoring", "KPI", "portfolio review", "reporting"]
        priority: medium

      deal-execution:
        description: "Deal pipeline, IC process, term sheets, closing procedures"
        seed_keywords: ["deal", "IC", "term sheet", "closing", "pipeline"]
        priority: high

    client-solutions:
      client-onboarding:
        description: "Onboarding process, KYC, subscription documents"
        seed_keywords: ["onboarding", "KYC", "subscription", "client setup"]
        priority: high

      product-knowledge:
        description: "Fund structures, evergreen vs closed-end, fee structures"
        seed_keywords: ["evergreen", "closed-end", "ELTIF", "fee", "fund structure"]
        priority: high

    operations-technology:
      architecture-standards:
        description: "System architecture, API design, cloud infrastructure"
        seed_keywords: ["architecture", "API", "microservices", "cloud"]
        priority: medium

      code-standards:
        description: "Coding conventions, PR process, testing requirements"
        seed_keywords: ["code style", "PR", "testing", "CI/CD", "linting"]
        priority: medium

      security-standards:
        description: "InfoSec policies, access control, incident response"
        seed_keywords: ["security", "access control", "incident", "penetration"]
        priority: high

    # Additional departments follow same pattern...

  teams:
    # Team-level topics are typically discovered during Phase 2
    # Seed with known high-priority items
    investments-pe-tech:
      tech-sector-thesis:
        description: "Current technology sector investment themes and criteria"
        seed_keywords: ["SaaS", "ARR", "tech thesis", "Rule of 40"]
        priority: high

      deal-memo-template:
        description: "PE Tech team-specific deal memorandum format"
        priority: medium

    engineering-platform:
      api-conventions:
        description: "REST API naming, versioning, error handling conventions"
        priority: medium

      deployment-runbook:
        description: "Deployment procedures, rollback, monitoring setup"
        priority: medium
  ```

- Validate taxonomy with 2–3 department representatives (30-min interviews each)
- Document data source inventory: list every known source, its owner, access method, and estimated document volume

**Deliverables**: `org_chart.yaml`, `topic_taxonomy.yaml`, data source inventory spreadsheet

**Estimated Effort**: 1 developer + 1 business analyst × 1 week (includes stakeholder interviews)

---

## Phase 1: Manual-Seed MVP (Weeks 3–6)

### 1.1 — Core Data Models & Types (Week 3)

**Objective**: Define all shared data structures used across the system.

**Tasks**:

- Implement core data models:
  ```python
  # src/common/models.py

  @dataclass
  class RawDocument:
      id: str
      source: str                      # "confluence", "gdrive", "github", etc.
      title: str
      content: str                     # Normalized to Markdown
      content_type: str                # "policy", "guide", "code", "template"
      metadata: DocumentMetadata

  @dataclass
  class DocumentMetadata:
      author: str
      department: Optional[str]
      team: Optional[str]
      created_at: datetime
      updated_at: datetime
      access_level: str                # "public", "internal", "confidential"
      tags: List[str]
      org_path: str                    # "Engineering/Platform/Auth"
      source_url: Optional[str]

  @dataclass
  class Chunk:
      id: str
      document_id: str
      content: str
      heading_path: List[str]          # Breadcrumb: ["Annual Report", "Investments", "PE"]
      position: int
      token_count: int
      parent_chunk_id: Optional[str]
      metadata: DocumentMetadata

  @dataclass
  class ClassifiedChunk:
      chunk: Chunk
      skill_category: str              # From topic_taxonomy
      hierarchy_level: str             # "corporate" | "department" | "team"
      department: Optional[str]
      team: Optional[str]
      confidence: float
      classification_method: str       # "metadata_rule" | "llm_content_analysis"
      reasoning: str

  @dataclass
  class PlannedSkill:
      name: str
      description: str
      level: str
      department: Optional[str]
      team: Optional[str]
      source_chunk_ids: List[str]
      depends_on: List[str]
      estimated_lines: int
      priority: str

  @dataclass
  class GeneratedSkill:
      plan: PlannedSkill
      skill_md: str                    # Full SKILL.md content
      reference_files: Dict[str, str]  # filename → content
      source_chunk_ids: List[str]
      generation_metadata: dict
      qa_result: Optional[QAReport]
      version: str
      status: str                      # "draft" | "review" | "published"
  ```

- Implement configuration loaders for `org_chart.yaml` and `topic_taxonomy.yaml`
- Write unit tests for all data models and config loading

**Deliverables**: `src/common/` package with all models, config loaders, utility functions

**Estimated Effort**: 1 developer × 1 week

---

### 1.2 — Document Preprocessor (Week 3–4)

**Objective**: Build the ingestion pipeline that converts raw documents to classified chunks.

**Tasks**:

- Implement format converters:
  - PDF → Markdown (via `pymupdf` or `docling`)
  - DOCX → Markdown (via `pandoc` or `python-docx`)
  - HTML → Markdown (via `markdownify` or `trafilatura`)
  - Plain text passthrough
  - Code files → Markdown with language tags

- Implement `SemanticChunker`:
  ```python
  class SemanticChunker:
      def __init__(self, max_chunk_tokens: int = 1500, min_chunk_tokens: int = 100):
          self.max = max_chunk_tokens
          self.min = min_chunk_tokens

      def chunk(self, document: RawDocument) -> List[Chunk]:
          # 1. Parse Markdown heading structure
          sections = self._split_by_headings(document.content)

          # 2. For each section, check token count
          chunks = []
          for section in sections:
              if section.token_count <= self.max:
                  chunks.append(self._to_chunk(section, document))
              else:
                  # Sub-split by paragraphs
                  sub_chunks = self._split_by_paragraphs(section)
                  chunks.extend(sub_chunks)

          # 3. Merge tiny chunks with siblings
          chunks = self._merge_small_chunks(chunks)

          # 4. Assign parent-child relationships
          self._assign_hierarchy(chunks)

          return chunks
  ```

- Implement manual file loader (for Phase 1, files are manually placed in a directory):
  ```python
  class ManualFileConnector:
      def __init__(self, directory: str):
          self.dir = directory

      def fetch_documents(self) -> List[RawDocument]:
          # Scan directory for supported file types
          # Convert each to RawDocument with manual metadata from sidecar .meta.yaml
          pass
  ```

- Write integration tests with sample documents (brand guide PDF, policy DOCX, code README)

**Deliverables**: `src/ingestion/` package (format converters, chunker, manual connector)

**Estimated Effort**: 1 developer × 1.5 weeks

---

### 1.3 — Hierarchy Classifier (Week 4–5)

**Objective**: Build the two-stage hierarchy classification system (metadata rules + LLM content analysis).

**Tasks**:

- Implement metadata-based rule classifier:
  ```python
  class MetadataClassifier:
      def __init__(self, org_chart: OrgChart, taxonomy: TopicTaxonomy):
          self.org = org_chart
          self.taxonomy = taxonomy

      def classify(self, chunk: Chunk) -> Optional[ClassifiedChunk]:
          # Rule 1: Source path mapping
          level = self._match_source_path(chunk.metadata.source_url)

          # Rule 2: Access level heuristic
          if chunk.metadata.access_level == "all_company":
              level = level or "corporate"

          # Rule 3: Author's org position
          if chunk.metadata.author:
              dept = self.org.get_department(chunk.metadata.author)
              team = self.org.get_team(chunk.metadata.author)

          # Rule 4: Keyword matching against taxonomy
          category = self.taxonomy.match_keywords(chunk.content)

          if level and category and confidence > 0.8:
              return ClassifiedChunk(...)
          return None  # Fall through to LLM
  ```

- Implement LLM content classifier:
  ```python
  class LLMContentClassifier:
      def __init__(self, llm_client, org_chart, taxonomy):
          self.llm = llm_client
          self.org = org_chart
          self.taxonomy = taxonomy

      async def classify(self, chunk: Chunk) -> ClassifiedChunk:
          # Build prompt with org chart + taxonomy + chunk content
          # Return structured classification result
          # Handle batch classification for efficiency (group 5-10 chunks per call)
          pass

      async def batch_classify(self, chunks: List[Chunk]) -> List[ClassifiedChunk]:
          # Process in batches of 5-10 for cost efficiency
          # Use Claude Haiku for classification (cheaper, fast enough)
          pass
  ```

- Implement combined classifier pipeline:
  ```python
  class HierarchyClassifier:
      async def classify(self, chunk: Chunk) -> ClassifiedChunk:
          # Try metadata rules first (free, instant)
          result = self.metadata_classifier.classify(chunk)
          if result and result.confidence >= 0.8:
              return result

          # Fall back to LLM analysis
          result = await self.llm_classifier.classify(chunk)
          if result.confidence < 0.7:
              result.needs_review = True
          return result
  ```

- Write evaluation tests: manually label 50 chunks, measure classification accuracy
- Target: >85% accuracy on hierarchy level, >80% on specific department/team assignment

**Deliverables**: `src/classification/` package, evaluation report on test set

**Estimated Effort**: 1 developer × 1.5 weeks

---

### 1.4 — Skill Generation Engine (Week 5–6)

**Objective**: Build the three-stage Skill generation pipeline.

**Tasks**:

- Implement `KnowledgeAggregator` (Stage 1):
  ```python
  class KnowledgeAggregator:
      async def aggregate(
          self,
          chunks: List[ClassifiedChunk],
          taxonomy: TopicTaxonomy,
          level: str
      ) -> List[KnowledgeTopic]:
          # 1. Group chunks by taxonomy category
          # 2. For each group, use LLM to identify sub-topics
          # 3. Map to existing taxonomy nodes or propose new ones
          # 4. Return list of KnowledgeTopic with chunk assignments
          pass
  ```

- Implement `SkillPlanner` (Stage 2):
  ```python
  class SkillPlanner:
      async def plan(
          self,
          topics: List[KnowledgeTopic],
          existing_skills: List[SkillMetadata],
          org_chart: OrgChart
      ) -> SkillPlan:
          # 1. Organize topics into corporate/department/team buckets
          # 2. Determine Skill boundaries (split large topics, merge small ones)
          # 3. Establish depends_on relationships
          # 4. Estimate line counts
          # 5. Output SkillPlan for human review (Phase 1: always review)
          pass
  ```

- Implement `SkillWriter` (Stage 3):
  ```python
  class SkillWriter:
      SKILL_TEMPLATE = """---
  name: {name}
  description: >-
    {description}
  level: {level}
  department: {department}
  team: {team}
  depends_on: {depends_on}
  sources: {sources}
  generated_at: {timestamp}
  version: {version}
  ---

  # {title}

  {body}
  """

      async def write_skill(
          self,
          plan: PlannedSkill,
          source_chunks: List[Chunk],
          parent_skills: List[str]
      ) -> GeneratedSkill:
          # 1. Compose prompt with:
          #    - Skill plan (name, level, description)
          #    - Parent skill summaries (to avoid repetition)
          #    - Source chunks (the actual knowledge)
          #    - Writing guidelines (imperative tone, <500 lines, etc.)
          # 2. Call LLM (Claude Sonnet for writing quality)
          # 3. Post-process: validate YAML frontmatter, check line count
          # 4. If > 500 lines, split into SKILL.md + references/
          pass

      async def write_all(self, plan: SkillPlan, ...) -> SkillRegistry:
          # Generate top-down: Corporate → Department → Team
          # Each level receives parent summaries to enable referencing
          pass
  ```

- Implement prompt templates library:
  - `prompts/classify_content.txt` — hierarchy classification prompt
  - `prompts/aggregate_topics.txt` — knowledge aggregation prompt
  - `prompts/plan_skills.txt` — skill planning prompt
  - `prompts/write_skill.txt` — skill writing prompt
  - `prompts/dedup_check.txt` — check for redundancy with parent skills

- Build CLI tool for manual pipeline execution:
  ```bash
  # Full pipeline
  python -m auto_skill_gen run \
    --input ./documents/ \
    --org-chart ./config/org_chart.yaml \
    --taxonomy ./config/topic_taxonomy.yaml \
    --output ./skills/

  # Individual stages
  python -m auto_skill_gen ingest --input ./documents/
  python -m auto_skill_gen classify --chunks-db ./data/chunks.json
  python -m auto_skill_gen plan --classified ./data/classified.json
  python -m auto_skill_gen generate --plan ./data/plan.json
  ```

**Deliverables**: `src/generation/` package, CLI tool, prompt templates, 5–10 generated Corporate Skills

**Estimated Effort**: 2 developers × 2 weeks

---

### 1.5 — Phase 1 Validation & Review (Week 6)

**Objective**: Validate generated Skills with stakeholders.

**Tasks**:

- Generate initial Corporate-level Skills from 10–20 hand-picked documents:
  - `corporate/brand-identity/SKILL.md`
  - `corporate/glossary/SKILL.md`
  - `corporate/compliance/SKILL.md`
  - `corporate/values-culture/SKILL.md`
  - `corporate/sustainability-esg/SKILL.md`

- Conduct review sessions with:
  - Marketing/Brand team → brand-identity Skill
  - Legal/Compliance → compliance Skill
  - Senior leadership → values-culture Skill
  - ESG team → sustainability Skill

- Document feedback: accuracy issues, missing content, wrong emphasis, incorrect terminology

- Iterate: revise prompts and re-generate based on feedback (2–3 iterations expected)

- Write retrospective: what worked, what to automate in Phase 2

**Deliverables**: 5–10 validated Corporate Skills, stakeholder feedback log, Phase 1 retrospective

**Estimated Effort**: 1 developer + 1 BA × 1 week

---

### Phase 1 Exit Criteria

- [ ] 5+ Corporate-level Skills generated and validated by subject-matter experts
- [ ] Classification accuracy >85% on manually labeled test set (50+ chunks)
- [ ] End-to-end pipeline runs via CLI (manual input → generated Skills)
- [ ] All core data models implemented with unit tests
- [ ] Stakeholder buy-in for Phase 2 scope

---

## Phase 2: Automated Ingestion & Three-Level Generation (Weeks 7–12)

### 2.1 — Source Connectors (Weeks 7–8)

**Objective**: Build automated connectors for primary data sources.

**Tasks**:

- Implement connector framework with common interface:
  ```python
  class SourceConnector(ABC):
      @abstractmethod
      async def fetch_documents(self, since: Optional[datetime] = None) -> List[RawDocument]:
          """Fetch documents, optionally only those modified since `since`."""
          pass

      @abstractmethod
      async def test_connection(self) -> bool:
          pass
  ```

- Build priority connectors (order by expected document volume and value):

  | Connector | Week | Integration Method | Notes |
  |-----------|------|--------------------|-------|
  | Confluence | 7 | REST API v2 | Spaces → pages → content |
  | Google Drive | 7 | Google Drive API v3 | Recursive folder scan, export to Markdown |
  | SharePoint / OneDrive | 8 | Microsoft Graph API | Similar to GDrive |
  | GitHub / GitLab | 8 | Git API + cloning | README, docs/, ADRs, CONTRIBUTING |
  | Public website | 8 | Web scraper (Playwright) | partnersgroup.com pages |

- Implement `source_config.yaml` with credentials (encrypted at rest):
  ```yaml
  sources:
    confluence:
      base_url: "https://partnersgroup.atlassian.net"
      auth: "oauth2"
      spaces: ["BRAND", "INVEST", "ENG", "COMPLY"]
      exclude_labels: ["draft", "archived"]
      sync_interval: "daily"

    gdrive:
      service_account: "config/gdrive_sa.json"
      root_folders:
        - id: "abc123"
          label: "Company Policies"
          department: null  # corporate-level
        - id: "def456"
          label: "Investment Handbooks"
          department: "Investments"
      file_types: ["docx", "pdf", "pptx", "md"]
      sync_interval: "daily"

    github:
      org: "partnersgroup"
      repos: ["platform-api", "data-pipeline", "infra"]
      paths: ["README.md", "docs/**", "ADR/**"]
      sync_interval: "on_push"  # webhook-triggered
  ```

- Build source-to-metadata mapper: infer `department` and `team` from source location
  ```python
  # Confluence space "ENG" → department: "Operations & Technology"
  # GDrive folder "Investment Handbooks" → department: "Investments"
  # GitHub repo "platform-api" → team: "Platform Engineering"
  ```

- Write integration tests with mock APIs and real API sandbox environments

**Deliverables**: 5 source connectors, source configuration system, integration tests

**Estimated Effort**: 2 developers × 2 weeks

---

### 2.2 — Embedding & Vector Store (Week 9)

**Objective**: Set up vectorization pipeline for semantic retrieval.

**Tasks**:

- Select and provision vector database (recommended: Qdrant self-hosted or Pinecone managed)

- Implement embedding pipeline:
  ```python
  class EmbeddingPipeline:
      def __init__(self, model: str = "voyage-3", vector_store: VectorStore):
          self.embedder = VoyageEmbedder(model)
          self.store = vector_store

      async def index_chunks(self, chunks: List[Chunk]):
          # Batch embed (max 128 chunks per API call for Voyage)
          embeddings = await self.embedder.batch_embed(
              [c.content for c in chunks],
              batch_size=128
          )

          # Upsert with rich metadata for filtering
          for chunk, embedding in zip(chunks, embeddings):
              await self.store.upsert(
                  id=chunk.id,
                  vector=embedding,
                  metadata={
                      "document_id": chunk.document_id,
                      "department": chunk.metadata.department,
                      "team": chunk.metadata.team,
                      "content_type": chunk.metadata.content_type,
                      "access_level": chunk.metadata.access_level,
                      "updated_at": chunk.metadata.updated_at.isoformat(),
                      "heading_path": "/".join(chunk.heading_path),
                  }
              )

      async def retrieve(
          self,
          query: str,
          filters: Optional[dict] = None,
          top_k: int = 20
      ) -> List[ScoredChunk]:
          query_embedding = await self.embedder.embed(query)
          results = await self.store.search(
              vector=query_embedding,
              filter=filters,
              limit=top_k
          )
          return results
  ```

- Implement metadata-filtered retrieval (critical for hierarchy-aware generation):
  ```python
  # Retrieve only chunks from Investments department
  chunks = await pipeline.retrieve(
      query="valuation methodology for SaaS companies",
      filters={"department": "Investments"},
      top_k=15
  )
  ```

- Write indexing benchmark: measure index build time and retrieval latency for expected corpus size (estimate: 5,000–20,000 chunks)

**Deliverables**: Embedding pipeline, vector store integration, retrieval benchmarks

**Estimated Effort**: 1 developer × 1 week

---

### 2.3 — Full Three-Level Generation Pipeline (Weeks 10–11)

**Objective**: Extend the MVP generation engine to produce Department and Team level Skills.

**Tasks**:

- Implement `HierarchicalAggregator` — top-down aggregation with deduplication:
  ```python
  class HierarchicalAggregator:

      async def aggregate_all(self, classified_chunks: List[ClassifiedChunk]) -> SkillTree:
          # Step 1: Corporate level
          corp_chunks = self._filter(classified_chunks, level="corporate")
          corp_topics = await self._cluster(corp_chunks)
          corp_skills = await self._plan_skills(corp_topics, parent_context=None)

          # Step 2: Department level (one department at a time)
          dept_skills = {}
          for dept in self.org.departments:
              dept_chunks = self._filter(classified_chunks, level="department", department=dept.name)
              # Remove content already covered by corporate skills
              dept_chunks = await self._dedup_against(dept_chunks, corp_skills)
              dept_topics = await self._cluster(dept_chunks)
              dept_skills[dept.name] = await self._plan_skills(
                  dept_topics, parent_context=corp_skills
              )

          # Step 3: Team level
          team_skills = {}
          for dept in self.org.departments:
              for team in dept.teams:
                  team_chunks = self._filter(classified_chunks, level="team", team=team.name)
                  parent = corp_skills + dept_skills.get(dept.name, [])
                  team_chunks = await self._dedup_against(team_chunks, parent)
                  if not team_chunks:
                      continue  # No unique team-level content
                  team_topics = await self._cluster(team_chunks)
                  team_skills[team.name] = await self._plan_skills(
                      team_topics, parent_context=parent
                  )

          return SkillTree(corp_skills, dept_skills, team_skills)
  ```

- Implement cross-level dependency resolver:
  ```python
  class DependencyResolver:
      def resolve(self, skill_tree: SkillTree) -> SkillTree:
          # For each department/team skill, determine which corporate/department
          # skills it should reference via depends_on
          # Based on: shared terminology, referenced concepts, parent scope overlap
          pass
  ```

- Implement `SkillPlanReview` — generates a human-readable plan for approval:
  ```python
  class SkillPlanReview:
      def generate_review(self, skill_tree: SkillTree) -> str:
          # Output a Markdown table of all planned skills:
          # | Level | Dept | Team | Skill Name | Sources | Est. Lines | Priority |
          # Plus: proposed new topics (not in taxonomy), unclassified chunks
          pass
  ```

- Build batch generation orchestrator:
  ```python
  class BatchGenerator:
      async def generate_all(self, approved_plan: SkillPlan) -> List[GeneratedSkill]:
          results = []

          # Phase A: Generate all Corporate skills (no dependencies)
          corp_results = await asyncio.gather(*[
              self.writer.write_skill(s, ...) for s in approved_plan.corporate_skills
          ])
          results.extend(corp_results)

          # Phase B: Generate Department skills (depends on Corporate)
          corp_summaries = self._summarize(corp_results)
          for dept, skills in approved_plan.department_skills.items():
              dept_results = await asyncio.gather(*[
                  self.writer.write_skill(s, parent_skills=corp_summaries, ...)
                  for s in skills
              ])
              results.extend(dept_results)

          # Phase C: Generate Team skills (depends on Corporate + Department)
          # ... similar pattern

          return results
  ```

- Implement Skill file writer (writes to disk in correct directory structure):
  ```python
  class SkillFileWriter:
      def write_to_disk(self, skill: GeneratedSkill, base_dir: str):
          # Determine path: skills/{level}/{dept?}/{team?}/{skill_name}/SKILL.md
          path = self._resolve_path(skill)
          os.makedirs(path, exist_ok=True)

          # Write SKILL.md
          with open(os.path.join(path, "SKILL.md"), "w") as f:
              f.write(skill.skill_md)

          # Write reference files if any
          if skill.reference_files:
              ref_dir = os.path.join(path, "references")
              os.makedirs(ref_dir, exist_ok=True)
              for filename, content in skill.reference_files.items():
                  with open(os.path.join(ref_dir, filename), "w") as f:
                      f.write(content)

      def write_registry(self, skills: List[GeneratedSkill], base_dir: str):
          # Generate registry.json with all skill metadata
          pass
  ```

- Generate first full three-level Skill tree (targeting 2–3 departments)

**Deliverables**: Full hierarchical generation pipeline, first multi-level Skill tree, plan review tool

**Estimated Effort**: 2 developers × 2 weeks

---

### 2.4 — Basic QA Pipeline (Week 12)

**Objective**: Implement automated quality checks before Skills are published.

**Tasks**:

- Implement structural checks:
  ```python
  class StructuralQA:
      def check(self, skill: GeneratedSkill) -> List[QACheck]:
          checks = []
          checks.append(self.check_frontmatter_valid(skill))     # Valid YAML
          checks.append(self.check_required_fields(skill))        # name, description, level
          checks.append(self.check_line_count(skill, max=500))    # Under 500 lines
          checks.append(self.check_heading_structure(skill))      # H1 → H2 → H3 ordered
          checks.append(self.check_no_empty_sections(skill))      # No headings with no content
          checks.append(self.check_depends_on_valid(skill))       # Referenced skills exist
          return checks
  ```

- Implement content quality checks (LLM-based):
  ```python
  class ContentQA:
      async def check(self, skill: GeneratedSkill) -> List[QACheck]:
          checks = []
          checks.append(await self.check_accuracy(skill))         # Consistent with sources
          checks.append(await self.check_completeness(skill))     # Covers key topics
          checks.append(await self.check_redundancy(skill))       # Not duplicating parent
          checks.append(await self.check_actionability(skill))    # Instructions are concrete
          checks.append(await self.check_trigger_coverage(skill)) # Description triggers well
          return checks
  ```

- Implement security checks:
  ```python
  class SecurityQA:
      def check(self, skill: GeneratedSkill) -> List[QACheck]:
          checks = []
          checks.append(self.check_no_secrets(skill))       # No API keys, passwords
          checks.append(self.check_no_pii(skill))           # No personal data
          checks.append(self.check_access_level(skill))     # Correct confidentiality
          return checks
  ```

- Build QA report generator (Markdown format for review)

- Define pass/fail thresholds:
  ```yaml
  qa_thresholds:
    auto_publish:
      structural: all_pass
      content_accuracy: >= 0.9
      security: all_pass
    needs_review:
      structural: all_pass
      content_accuracy: >= 0.7
      security: all_pass
    rejected:
      any: fail
  ```

**Deliverables**: QA pipeline (`src/qa/`), QA report templates, threshold configuration

**Estimated Effort**: 1 developer × 1 week

---

### Phase 2 Exit Criteria

- [ ] 3+ source connectors operational (Confluence, GDrive, GitHub minimum)
- [ ] Vector store indexed with full document corpus
- [ ] Three-level Skill tree generated for 2–3 departments
- [ ] QA pipeline catching structural, content, and security issues
- [ ] End-to-end pipeline: source → ingest → classify → plan → generate → QA → publish
- [ ] Total generated Skills: 15–30 across all levels

---

## Phase 3: Incremental Updates & Review Dashboard (Weeks 13–18)

### 3.1 — Change Detection System (Weeks 13–14)

**Objective**: Detect when source documents change and identify which Skills need updating.

**Tasks**:

- Implement change detection per connector:
  ```python
  class ChangeDetector:
      def __init__(self, connectors: List[SourceConnector], state_store: StateStore):
          self.connectors = connectors
          self.state = state_store  # Tracks last sync timestamps, document hashes

      async def detect(self) -> ChangeReport:
          changes = ChangeReport()

          for connector in self.connectors:
              last_sync = self.state.get_last_sync(connector.name)
              new_docs = await connector.fetch_documents(since=last_sync)

              for doc in new_docs:
                  prev_hash = self.state.get_hash(doc.id)
                  curr_hash = self._hash_content(doc.content)

                  if prev_hash is None:
                      changes.add(ChangeType.NEW, doc)
                  elif prev_hash != curr_hash:
                      diff = self._compute_diff(
                          self.state.get_content(doc.id), doc.content
                      )
                      if diff.significance > 0.1:  # Filter trivial edits
                          changes.add(ChangeType.MODIFIED, doc, diff=diff)

              # Detect deletions
              prev_ids = self.state.get_document_ids(connector.name)
              curr_ids = {d.id for d in new_docs}
              for deleted_id in prev_ids - curr_ids:
                  changes.add(ChangeType.DELETED, doc_id=deleted_id)

              self.state.update_sync(connector.name, datetime.now())

          return changes
  ```

- Implement impact analysis:
  ```python
  class ImpactAnalyzer:
      def analyze(self, changes: ChangeReport, registry: SkillRegistry) -> List[ImpactedSkill]:
          impacted = []
          for change in changes:
              # Find all chunks from this document
              chunk_ids = self.chunk_store.get_chunks_by_document(change.document_id)

              # Find all skills that use these chunks
              for chunk_id in chunk_ids:
                  skills = registry.find_skills_using_chunk(chunk_id)
                  for skill in skills:
                      impacted.append(ImpactedSkill(
                          skill=skill,
                          change=change,
                          severity=self._assess_severity(change, skill)
                      ))

          return self._deduplicate(impacted)
  ```

- Implement scheduling:
  ```python
  # config/schedule.yaml
  schedules:
    confluence:
      type: cron
      expression: "0 2 * * *"   # Daily at 2 AM
    github:
      type: webhook
      event: "push"
      branches: ["main"]
    gdrive:
      type: cron
      expression: "0 3 * * 1"   # Weekly on Monday at 3 AM
  ```

- Build change notification system (Slack/email alerts for detected changes)

**Deliverables**: Change detection system, impact analyzer, scheduling configuration, notifications

**Estimated Effort**: 2 developers × 2 weeks

---

### 3.2 — Incremental Regeneration Engine (Weeks 15–16)

**Objective**: Efficiently re-generate only the affected Skills when sources change.

**Tasks**:

- Implement partial regeneration pipeline:
  ```python
  class IncrementalRegenerator:

      async def regenerate(self, impacted_skills: List[ImpactedSkill]):
          for impact in impacted_skills:
              skill = impact.skill

              # 1. Re-collect all source chunks for this skill (including new/changed ones)
              source_chunks = await self._gather_current_sources(skill)

              # 2. Re-classify if needed (new chunks may change hierarchy assignment)
              reclassified = await self.classifier.batch_classify(
                  [c for c in source_chunks if c.is_new or c.is_modified]
              )

              # 3. Check if hierarchy level changed
              if self._hierarchy_changed(reclassified, skill):
                  # Flag for manual review — level changes are significant
                  self._flag_for_review(skill, reason="hierarchy_level_change")
                  continue

              # 4. Re-generate the skill
              parent_skills = await self._get_parent_summaries(skill)
              new_version = await self.writer.write_skill(
                  skill.plan, source_chunks, parent_skills
              )

              # 5. Diff against current version
              diff = self._diff_skills(skill.current_content, new_version.skill_md)

              # 6. If diff is trivial, skip update
              if diff.significance < 0.05:
                  self._log("Skipping trivial update", skill=skill.name)
                  continue

              # 7. Run QA
              qa_result = await self.qa.check(new_version)

              # 8. Version bump and publish/queue
              new_version.version = self._bump_version(skill.version)
              new_version.changelog = diff.summary

              if qa_result.auto_publishable:
                  await self.registry.publish(new_version)
              else:
                  await self.registry.queue_for_review(new_version, qa_result)
  ```

- Implement version management:
  ```python
  class VersionManager:
      def bump(self, current: str, change_type: str) -> str:
          major, minor, patch = map(int, current.split("."))
          if change_type == "content_update":
              return f"{major}.{minor}.{patch + 1}"
          elif change_type == "structural_change":
              return f"{major}.{minor + 1}.0"
          elif change_type == "hierarchy_change":
              return f"{major + 1}.0.0"
  ```

- Implement changelog generation:
  ```python
  class ChangelogGenerator:
      async def generate(self, old_skill: str, new_skill: str, change: Change) -> str:
          prompt = f"""
          Compare the old and new versions of this Skill and write a concise changelog.
          Focus on: added content, removed content, changed definitions, updated references.

          Old version:
          {old_skill[:2000]}

          New version:
          {new_skill[:2000]}

          Source change:
          {change.summary}

          Return: 3-5 bullet points describing the changes.
          """
          return await self.llm.generate(prompt)
  ```

- Implement cascade update detection:
  ```python
  # When a Corporate skill changes, check if Department/Team skills
  # that depend_on it need updating too
  class CascadeDetector:
      def detect(self, updated_skill: GeneratedSkill, registry: SkillRegistry) -> List[str]:
          dependents = registry.find_dependents(updated_skill.plan.name)
          # For each dependent, check if the change affects the referenced content
          return [d for d in dependents if self._is_affected(d, updated_skill)]
  ```

**Deliverables**: Incremental regeneration engine, version management, changelog generation, cascade detection

**Estimated Effort**: 2 developers × 2 weeks

---

### 3.3 — Review Dashboard (Weeks 17–18)

**Objective**: Build a web UI for human review and approval of generated/updated Skills.

**Tasks**:

- Build backend API (FastAPI):
  ```python
  # Endpoints:
  # GET  /api/skills                    — List all skills with status
  # GET  /api/skills/{name}             — Get skill detail + history
  # GET  /api/skills/{name}/diff/{v1}/{v2} — Diff between versions
  # GET  /api/review/queue              — Skills pending review
  # POST /api/review/{name}/approve     — Approve a skill version
  # POST /api/review/{name}/reject      — Reject with comments
  # POST /api/review/{name}/edit        — Submit manual edits
  # GET  /api/changes/recent            — Recent source document changes
  # GET  /api/metrics                   — System health metrics
  ```

- Build frontend (React or Streamlit for MVP):
  - **Dashboard view**: Overall stats (total skills, pending reviews, recent changes)
  - **Review queue**: List of skills needing approval, sorted by priority
  - **Skill detail view**: Current content, diff against previous version, source chunks, QA report
  - **Skill tree browser**: Navigate the corporate → department → team hierarchy
  - **Change log**: History of all changes with source attribution

- Implement RBAC (role-based access control):
  ```yaml
  roles:
    admin:
      permissions: ["review_all", "publish", "reject", "edit_taxonomy", "manage_sources"]
    department_reviewer:
      permissions: ["review_department", "publish_department", "suggest_edits"]
      scope: "{department}"   # Can only review their department's skills
    viewer:
      permissions: ["read_all"]
  ```

- Implement Slack/Teams integration for review notifications:
  ```
  🔔 New Skill for Review
  📄 dept-investments-valuation v1.2
  ✅ QA Score: 88/100 (2 warnings)
  ⚠️ Warning: Possible redundancy with corporate/glossary
  [Review Now] [Approve] [Skip]
  ```

**Deliverables**: Review dashboard (API + UI), RBAC system, notification integration

**Estimated Effort**: 2 developers × 2 weeks

---

### Phase 3 Exit Criteria

- [ ] Change detection running on schedule for all connected sources
- [ ] Incremental regeneration producing versioned updates with changelogs
- [ ] Review dashboard operational with RBAC
- [ ] At least one full change-detection → regeneration → review → publish cycle completed
- [ ] Cascade updates working (corporate change triggers downstream review)

---

## Phase 4: Agent Integration & Feedback Loop (Weeks 19–22)

### 4.1 — Agent Skill Loader (Weeks 19–20)

**Objective**: Enable AI Agents to dynamically load Skills based on their identity.

**Tasks**:

- Implement Skill Loader API:
  ```python
  class SkillLoader:
      def __init__(self, registry: SkillRegistry):
          self.registry = registry

      def load_for_agent(
          self,
          agent_id: str,
          department: str,
          team: str,
          context: Optional[str] = None
      ) -> LoadedSkillSet:
          skills = []

          # Layer 1: Always load Corporate (metadata only initially)
          corp_skills = self.registry.get(level="corporate", status="published")
          skills.extend(corp_skills)

          # Layer 2: Department skills
          dept_skills = self.registry.get(
              level="department", department=department, status="published"
          )
          skills.extend(dept_skills)

          # Layer 3: Team skills
          team_skills = self.registry.get(
              level="team", team=team, status="published"
          )
          skills.extend(team_skills)

          # Progressive disclosure: sort by priority, truncate if context window limited
          loaded = self._apply_progressive_disclosure(skills, context)

          return LoadedSkillSet(
              metadata=[s.frontmatter for s in loaded],
              full_content={s.name: s.skill_md for s in loaded if s.load_full},
          )
  ```

- Implement Skill hot-reload (update skills without restarting agents):
  ```python
  class SkillHotReloader:
      def __init__(self, registry: SkillRegistry, agents: AgentManager):
          self.registry = registry
          self.agents = agents

      async def on_skill_published(self, skill_name: str):
          # Find all agents using this skill
          affected_agents = self.agents.find_agents_using(skill_name)

          for agent in affected_agents:
              # Send reload signal
              await agent.reload_skill(skill_name)
              self._log(f"Reloaded {skill_name} for agent {agent.id}")
  ```

- Build Skill serving endpoint (REST/gRPC):
  ```
  GET /api/v1/skills/load?department=investments&team=pe-tech
  → Returns: { metadata: [...], skills: { "corporate/glossary": "...", ... } }
  ```

- Write integration tests simulating Agent startup and skill loading

**Deliverables**: Skill Loader library, serving API, hot-reload mechanism

**Estimated Effort**: 2 developers × 2 weeks

---

### 4.2 — Usage Tracking & Feedback Collection (Weeks 21–22)

**Objective**: Instrument Agent usage to understand Skill effectiveness and drive improvements.

**Tasks**:

- Implement usage event tracking:
  ```python
  class SkillUsageTracker:
      async def track(self, event: UsageEvent):
          # Store in time-series DB (InfluxDB, TimescaleDB, or simple Postgres)
          await self.store.insert({
              "timestamp": event.timestamp,
              "agent_id": event.agent_id,
              "skill_name": event.skill_name,
              "event_type": event.type,   # "triggered", "loaded", "referenced"
              "user_query": event.query_summary,  # Anonymized
              "output_quality": event.quality_signal,
              "context": event.context_metadata,
          })
  ```

- Define key metrics:
  ```python
  class SkillMetrics:
      def compute(self, skill_name: str, window: str = "30d") -> dict:
          return {
              # Usage metrics
              "trigger_count": ...,              # How often triggered
              "trigger_rate": ...,               # Triggered / should-have-triggered
              "false_positive_rate": ...,        # Triggered but wasn't helpful
              
              # Quality metrics
              "avg_output_quality": ...,         # User feedback score
              "user_correction_rate": ...,       # How often user corrects Agent output
              
              # Freshness metrics
              "days_since_update": ...,
              "source_docs_changed_since": ...,  # Source changes not yet reflected
              
              # Efficiency metrics
              "avg_tokens_in_context": ...,      # Context window usage
              "load_time_ms": ...,
          }
  ```

- Build feedback collection mechanisms:
  - **Implicit**: Track when Agent output gets corrected by user
  - **Explicit**: Thumbs up/down on Agent responses (attributed back to Skills used)
  - **Gap detection**: Log queries where no Skill was triggered but should have been
  ```python
  class GapDetector:
      async def detect_gaps(self, query: str, triggered_skills: List[str]) -> Optional[Gap]:
          # Use LLM to check: "Given this query, should any of our skills have been used?"
          prompt = f"""
          User query: {query}
          Available skills: {self.registry.list_metadata()}
          Triggered skills: {triggered_skills}

          Was there a skill that SHOULD have been triggered but wasn't?
          Or is there a knowledge gap — a topic this query needs that no skill covers?
          """
          result = await self.llm.generate(prompt)
          if result.gap_detected:
              return Gap(query=query, suggested_skill=result.suggestion)
          return None
  ```

- Build weekly metrics report:
  ```
  📊 Auto Skill Generator — Weekly Report (Feb 10–16, 2026)
  
  Total Skills: 47 (Corp: 8, Dept: 22, Team: 17)
  Skills Triggered: 1,284 times across 14 agents
  
  Top Performing:
  1. corporate/glossary — 342 triggers, 4.7/5 quality
  2. dept-investments/valuation — 198 triggers, 4.5/5 quality
  
  Needs Attention:
  ⚠️ team-eng-platform/deployment-runbook — 12% correction rate (above 5% threshold)
  ⚠️ dept-client/onboarding — 3 gap detections this week
  
  Pending Updates: 4 skills affected by source changes (review needed)
  ```

**Deliverables**: Usage tracking system, metrics dashboard, gap detector, weekly report generator

**Estimated Effort**: 2 developers × 2 weeks

---

### Phase 4 Exit Criteria

- [ ] Agents successfully loading Skills from registry at startup
- [ ] Hot-reload working (new Skill version → Agents update without restart)
- [ ] Usage tracking capturing trigger events, quality signals, and gaps
- [ ] Weekly metrics report generated automatically
- [ ] At least one Skill improved based on usage feedback

---

## Phase 5: Optimization & Scale (Weeks 23–26+)

### 5.1 — Cost Optimization (Week 23)

**Tasks**:

- Implement LLM call caching (same chunk content → same classification, skip re-processing)
- Implement tiered model usage:
  ```yaml
  model_strategy:
    classification: "claude-haiku-4-5"         # Cheap, fast
    aggregation: "claude-sonnet-4-5"           # Mid-tier
    skill_writing: "claude-sonnet-4-5"         # Quality matters
    skill_planning: "claude-opus-4-5"          # Complex reasoning
    qa_checks: "claude-haiku-4-5"              # Simple verification
  ```
- Implement batch processing (group API calls to reduce overhead)
- Add token usage tracking and budget alerts
- Profile and optimize embedding pipeline (cache embeddings for unchanged chunks)
- Estimated cost model:
  ```
  Initial full generation (5000 chunks, 50 skills):
    Classification: ~2M input tokens (Haiku) ≈ $1.60
    Generation: ~500K input + ~200K output (Sonnet) ≈ $4.50
    QA: ~300K input (Haiku) ≈ $0.24
    Embeddings: ~1M tokens (Voyage) ≈ $0.10
    Total: ~$6.50 per full run

  Incremental update (50 changed chunks, 3 skills):
    ~$0.40 per update cycle
  ```

**Deliverables**: Cost optimization implementation, usage monitoring, budget alert system

---

### 5.2 — Additional Source Connectors (Week 24)

**Tasks**:

- Implement remaining connectors:
  - Slack/Teams (pinned messages, channel topics, bookmarked threads)
  - Notion
  - JIRA/Asana (for process documentation embedded in tickets)
  - Email archives (if applicable, for policy announcements)
  - Internal training platform (LMS)
- Implement connector health monitoring and auto-retry with backoff

**Deliverables**: 3–5 additional connectors, health monitoring

---

### 5.3 — Multi-Language Support (Week 25)

**Tasks**:

- Implement language detection per chunk (for multilingual document corpora)
- Implement Skill generation in target language(s):
  ```python
  class MultiLangSkillWriter:
      async def write_skill(self, plan, chunks, lang="en"):
          # If source chunks are mixed language, normalize to target
          # Generate skill in target language
          # Maintain consistent terminology across languages (use glossary as anchor)
          pass
  ```
- Generate parallel Skills for key languages (e.g., English + German + Japanese for Partners Group's key markets)

**Deliverables**: Language detection, multi-language generation support

---

### 5.4 — Advanced Analytics & Self-Improvement (Week 26+)

**Tasks**:

- Implement Skill A/B testing framework:
  ```python
  # Route 50% of agents to Skill v1.3, 50% to v1.4
  # Compare output quality metrics between groups
  class SkillABTest:
      def assign_variant(self, agent_id: str, skill_name: str) -> str:
          # Deterministic assignment based on agent_id hash
          pass
  ```

- Implement auto-improvement pipeline:
  ```python
  class AutoImprover:
      async def suggest_improvements(self, skill_name: str):
          metrics = self.metrics.compute(skill_name)
          feedback = self.tracker.get_feedback(skill_name)
          corrections = self.tracker.get_corrections(skill_name)

          if metrics["user_correction_rate"] > 0.05:
              # Analyze corrections to identify systematic issues
              prompt = f"""
              This skill is being corrected by users {metrics['user_correction_rate']*100}% 
              of the time. Here are the corrections:
              {format_corrections(corrections)}

              Current skill content:
              {skill.content}

              What specific changes would fix these issues?
              """
              suggestions = await self.llm.generate(prompt)
              return suggestions
  ```

- Build taxonomy evolution tracker (visualize how the topic taxonomy grows over time)
- Implement Skill dependency graph visualization

**Deliverables**: A/B testing framework, auto-improvement pipeline, analytics visualizations

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| LLM classification inaccuracy | Medium | High | Seed taxonomy + human review loop; target >85% accuracy |
| Source document access denied | Medium | Medium | Early access negotiation; graceful degradation per source |
| Generated Skills contain hallucinations | Medium | High | Source-grounded generation; QA accuracy check; human review |
| Cost overrun on LLM API calls | Low | Medium | Tiered model strategy; caching; batch processing; budget alerts |
| Stakeholder resistance to automated content | Medium | Medium | Start with human-in-the-loop; show value with MVP; gradual trust |
| Stale Skills (sources change, skills don't) | Low | High | Change detection + scheduling; freshness metrics; Slack alerts |
| Context window overflow (too many skills loaded) | Low | Medium | Progressive disclosure; priority-based loading; summarization |
| Security: sensitive data in generated Skills | Medium | High | PII/secret scanning in QA; access-level filtering; review gate |

---

## Team & Resource Requirements

### Core Team

| Role | Headcount | Phase Coverage | Key Responsibilities |
|------|-----------|---------------|---------------------|
| Backend Engineer (Senior) | 1 | All phases | Architecture, LLM integration, generation engine |
| Backend Engineer (Mid) | 1 | Phase 2+ | Connectors, embedding pipeline, incremental updates |
| Full-Stack Engineer | 1 | Phase 3+ | Review dashboard, metrics UI, API endpoints |
| ML/NLP Engineer | 0.5 | Phase 1–2 | Classification tuning, embedding optimization |
| Business Analyst | 0.5 | Phase 0–1, 4 | Stakeholder interviews, taxonomy design, feedback analysis |
| Product Manager | 0.25 | All phases | Prioritization, stakeholder management |

### Infrastructure

| Resource | Specification | Estimated Monthly Cost |
|----------|--------------|----------------------|
| Vector Database (Qdrant Cloud or Pinecone) | 100K vectors, 1536 dimensions | $50–$150 |
| LLM API (Anthropic Claude) | ~10M tokens/month after initial build | $50–$200 |
| Embedding API (Voyage) | ~5M tokens/month | $5–$15 |
| Compute (API server + workers) | 2× medium instances | $100–$200 |
| Object Storage (Skills + documents) | <100 GB | $5 |
| CI/CD + monitoring | Standard tooling | $50 |
| **Total** | | **$260–$620/month** |

---

## Success Metrics

### Phase 1 (MVP)
- 5+ Corporate Skills generated and approved by SMEs
- Classification accuracy ≥ 85% on labeled test set

### Phase 2 (Automation)
- 3+ data sources connected and syncing
- 20+ Skills across all three levels
- Full pipeline execution time < 30 minutes for 5,000 chunks

### Phase 3 (Continuous)
- Change detection → regeneration cycle < 4 hours
- Review queue turnaround < 48 hours
- Zero undetected source changes older than 7 days

### Phase 4 (Integration)
- Agent Skill loading latency < 500ms
- Skill trigger accuracy ≥ 90% (triggered when should, not when shouldn't)
- User correction rate < 5% for Skill-informed Agent outputs

### Phase 5 (Optimization)
- Cost per Skill generation < $0.50
- Incremental update cost < $0.10 per affected Skill
- At least 1 Skill auto-improved based on feedback loop per month

---

## Appendix: Key Technical Decisions

### A. Why generate SKILL.md files instead of pure RAG?

SKILL.md provides pre-compiled, version-controlled, auditable knowledge that loads instantly. RAG provides dynamic retrieval but with variable results. The optimal approach is **both**: SKILL.md for stable procedural knowledge (processes, standards, terminology) and RAG for factual details (latest metrics, specific client info, recent events).

### B. Why top-down generation order?

Generating Corporate → Department → Team ensures each level can reference its parent without circular dependencies. It also enables effective deduplication: lower levels only contain knowledge not already present in higher levels.

### C. Why seed taxonomy instead of pure unsupervised clustering?

Unsupervised LLM clustering cannot guarantee business-relevant topic boundaries. A seed taxonomy provides deterministic coverage of known-important topics while still allowing discovery of new topics. This is a supervised-first, unsupervised-second approach.

### D. Why human review for new topics but not for routine updates?

New topics represent structural decisions about the knowledge hierarchy — these are business decisions, not technical ones. Routine content updates within existing topics can be safely automated with QA checks, as the structural decision has already been made.
