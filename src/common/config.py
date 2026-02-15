"""Configuration loaders for YAML config files.

Classes to implement:
    - OrgChart: Load and query org_chart.yaml
        - get_department(person) -> str
        - get_team(person) -> str
        - list_departments() -> List[Department]
        - list_teams(department) -> List[Team]

    - TopicTaxonomy: Load and query topic_taxonomy.yaml
        - match_keywords(content) -> Optional[str]
        - get_topics(level, department?, team?) -> List[Topic]
        - add_topic(level, category, topic) -> None

    - SourceConfig: Load source_config.yaml
        - get_connector_config(name) -> dict
        - list_sources() -> List[str]

    - GenerationConfig: Load generation_config.yaml
        - get_model(task) -> str
        - get_token_budget(task) -> int
        - get_batch_size(task) -> int
"""
