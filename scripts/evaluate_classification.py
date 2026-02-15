"""Classification accuracy evaluation script.

Purpose:
    Evaluates classification pipeline accuracy against a manually labeled test set.
    Targets: >85% hierarchy level accuracy, >80% department/team accuracy.

Usage:
    python scripts/evaluate_classification.py --labeled-data data/labeled_chunks.json --output reports/classification_eval.md

Expected input format (labeled_chunks.json):
    [
        {
            "chunk_id": "...",
            "content": "...",
            "expected_level": "corporate|department|team",
            "expected_department": "...",
            "expected_team": "...",
            "expected_category": "..."
        }
    ]
"""
