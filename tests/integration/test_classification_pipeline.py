"""Integration tests for the classification pipeline.

Tests to implement:
    - test_metadata_then_llm_fallback: Metadata rules → LLM for uncertain chunks
    - test_batch_classification: Classify batch of chunks end-to-end
    - test_classification_accuracy: Evaluate against labeled test set (target >85%)
"""
