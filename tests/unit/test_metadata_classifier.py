"""Tests for MetadataClassifier in src/classification/metadata_classifier.py.

Tests to implement:
    - test_source_path_mapping: Classifies by URL/path patterns
    - test_access_level_heuristic: all_company → corporate level
    - test_author_org_position: Looks up author in org chart
    - test_keyword_matching: Matches against taxonomy seed_keywords
    - test_high_confidence_return: Returns ClassifiedChunk when confidence >= 0.8
    - test_low_confidence_fallthrough: Returns None when confidence < 0.8
    - test_combined_rules: Multiple rules reinforce confidence
"""
