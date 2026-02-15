"""Helper script to bootstrap topic_taxonomy.yaml.

Purpose:
    Interactively builds the initial topic taxonomy by:
    1. Reading the org chart to understand department/team structure
    2. Prompting for key topics at each level
    3. Generating seed keywords via LLM suggestions
    4. Writing the result to config/topic_taxonomy.yaml

Usage:
    python scripts/seed_taxonomy.py --org-chart config/org_chart.yaml --output config/topic_taxonomy.yaml
"""
