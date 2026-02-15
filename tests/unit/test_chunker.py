"""Tests for SemanticChunker in src/ingestion/chunker.py.

Tests to implement:
    - test_split_by_headings: Correctly splits on H1/H2/H3
    - test_large_section_sub_split: Splits sections exceeding max_chunk_tokens
    - test_merge_small_chunks: Merges chunks below min_chunk_tokens
    - test_parent_child_hierarchy: Assigns correct parent-child relationships
    - test_heading_path_breadcrumbs: Builds correct heading_path for each chunk
    - test_empty_document: Handles empty input gracefully
    - test_no_headings_document: Handles documents with no Markdown headings
"""
