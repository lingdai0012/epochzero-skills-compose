# Auto Skill Generator — Concise Implementation Steps

> Automated SKILL.md generation from corporate documents across Corporate → Department → Team hierarchy.

---

## Phase 0: Foundation & Setup (Weeks 1–2)

1. **Set up monorepo** — `src/` with `connectors/`, `ingestion/`, `embedding/`, `classification/`, `generation/`, `qa/`, `registry/`, `common/`; `skills/` output dir; `config/`; `tests/`; `infra/`
2. **Configure Python project** — Python 3.11+, `pyproject.toml`, ruff, mypy, pytest
3. **Provision infrastructure** — Docker Compose (vector DB, task queue), cloud storage, LLM API keys, CI/CD pipeline
4. **Build `org_chart.yaml`** — Full company → departments → teams structure with focus areas and headcounts
5. **Build `topic_taxonomy.yaml`** — Seed topics at corporate/department/team levels with descriptions, keywords, and priorities
6. **Document data source inventory** — List all sources, owners, access methods, estimated volume

---

## Phase 1: Manual-Seed MVP (Weeks 3–6)

7. **Implement core data models** — `RawDocument`, `DocumentMetadata`, `Chunk`, `ClassifiedChunk`, `PlannedSkill`, `GeneratedSkill` dataclasses + config loaders + unit tests
8. **Build format converters** — PDF, DOCX, HTML, plain text, code → Markdown
9. **Build `SemanticChunker`** — Split by headings, sub-split by paragraphs, merge small chunks, assign parent-child hierarchy
10. **Build `ManualFileConnector`** — Scan local directory for files + sidecar `.meta.yaml` metadata
11. **Implement metadata-based rule classifier** — Classify chunks by source path, access level, author org position, keyword matching against taxonomy
12. **Implement LLM content classifier** — Batch classify chunks (5–10 per call) using Claude Haiku for cost efficiency
13. **Combine classifiers in pipeline** — Metadata rules first (free/instant), LLM fallback for low-confidence results
14. **Evaluate classification** — Label 50 chunks manually, target >85% hierarchy accuracy, >80% department/team accuracy
15. **Build `KnowledgeAggregator`** — Group chunks by taxonomy category, use LLM to identify sub-topics
16. **Build `SkillPlanner`** — Organize topics into levels, determine skill boundaries, establish `depends_on`, estimate sizes
17. **Build `SkillWriter`** — Compose prompts with plan + parent summaries + source chunks + writing guidelines; generate with Claude Sonnet; validate frontmatter; split >500 lines into SKILL.md + references/
18. **Create prompt templates** — `classify_content`, `aggregate_topics`, `plan_skills`, `write_skill`, `dedup_check`
19. **Build CLI tool** — `run`, `ingest`, `classify`, `plan`, `generate` subcommands
20. **Generate & validate 5–10 Corporate Skills** — brand-identity, glossary, compliance, values-culture, sustainability-esg
21. **Conduct stakeholder review sessions** — Iterate 2–3 times on prompts based on feedback

---

## Phase 2: Automated Ingestion & Three-Level Generation (Weeks 7–12)

22. **Implement connector framework** — Abstract `SourceConnector` with `fetch_documents(since)` and `test_connection()`
23. **Build source connectors** — Confluence (REST API v2), Google Drive (API v3), SharePoint (Graph API), GitHub/GitLab (Git API), public website (Playwright)
24. **Build `source_config.yaml`** — Credentials (encrypted), spaces/folders/repos to scan, sync intervals, exclusion rules
25. **Build source-to-metadata mapper** — Infer department/team from source location
26. **Set up vector database** — Qdrant or Pinecone
27. **Build embedding pipeline** — Batch embed with Voyage, upsert with rich metadata, support metadata-filtered retrieval
28. **Build `HierarchicalAggregator`** — Top-down: Corporate → Department → Team; deduplicate against parent levels at each step
29. **Build cross-level dependency resolver** — Determine `depends_on` from shared terminology and referenced concepts
30. **Build `SkillPlanReview`** — Generate human-readable Markdown plan table for approval
31. **Build `BatchGenerator`** — Generate Corporate (parallel) → Department (parallel per dept, depends on Corp) → Team (parallel per team, depends on Corp+Dept)
32. **Build `SkillFileWriter`** — Write to `skills/{level}/{dept?}/{team?}/{name}/SKILL.md` + references/ + registry.json
33. **Generate first full three-level Skill tree** for 2–3 departments
34. **Build QA pipeline** — Structural checks (frontmatter, line count, heading structure, deps valid), content checks (accuracy, completeness, redundancy, actionability), security checks (no secrets, no PII, correct access level)
35. **Define QA thresholds** — Auto-publish / needs-review / rejected based on scores

---

## Phase 3: Incremental Updates & Review Dashboard (Weeks 13–18)

36. **Build change detection** — Per-connector: fetch since last sync, hash comparison, diff significance filtering (>10%), deletion detection
37. **Build impact analyzer** — Map changed documents → affected chunks → affected skills with severity assessment
38. **Configure scheduling** — Cron (daily/weekly per source) and webhook triggers (GitHub push)
39. **Build change notifications** — Slack/email alerts for detected changes
40. **Build incremental regeneration engine** — Re-collect sources, re-classify new/changed chunks, re-generate skill, diff against current, skip trivial updates (<5% change), run QA, version bump
41. **Implement version management** — Semantic versioning: patch (content update), minor (structural change), major (hierarchy change)
42. **Build changelog generator** — LLM-generated 3–5 bullet points comparing old vs new versions
43. **Build cascade update detector** — When Corporate skill changes, check dependent Department/Team skills
44. **Build review dashboard backend** — FastAPI: list skills, get detail + history, diff versions, review queue, approve/reject/edit, recent changes, metrics
45. **Build review dashboard frontend** — Dashboard stats, review queue, skill detail with diff/sources/QA, skill tree browser, change log
46. **Implement RBAC** — Admin (all), department reviewer (scoped), viewer (read-only)
47. **Build Slack/Teams review notifications** — Skill name, QA score, warnings, action buttons

---

## Phase 4: Agent Integration & Feedback Loop (Weeks 19–22)

48. **Build Skill Loader API** — Load Corporate + Department + Team skills for agent identity; progressive disclosure by priority
49. **Build Skill serving endpoint** — REST/gRPC: `GET /skills/load?department=X&team=Y`
50. **Implement Skill hot-reload** — On publish, notify affected agents to reload without restart
51. **Build usage event tracking** — Track trigger, load, reference events per agent/skill with quality signals
52. **Define and compute key metrics** — Trigger count/rate, false positive rate, avg output quality, user correction rate, freshness, context token usage
53. **Build feedback collection** — Implicit (correction tracking), explicit (thumbs up/down), gap detection (queries where no skill triggered but should have)
54. **Build weekly metrics report** — Top performing skills, needs-attention skills, pending updates, gap detections

---

## Phase 5: Optimization & Scale (Weeks 23–26+)

55. **Optimize LLM costs** — Call caching, tiered model usage (Haiku for classification/QA, Sonnet for writing, Opus for planning), batch processing, token budget alerts
56. **Build additional source connectors** — Slack/Teams, Notion, JIRA/Asana, email archives, LMS
57. **Add multi-language support** — Language detection per chunk, generate skills in target languages, maintain terminology consistency via glossary
58. **Build Skill A/B testing framework** — Route agent variants to different skill versions, compare quality metrics
59. **Build auto-improvement pipeline** — Analyze user corrections for systematic issues, suggest skill changes via LLM
60. **Build analytics visualizations** — Taxonomy evolution tracker, skill dependency graph
