"""Integration tests for the full ingestion pipeline.

Tests to implement:
    - test_end_to_end_ingestion: Load sample documents → convert → chunk → verify output
    - test_pdf_to_chunks: PDF document → Markdown → chunks
    - test_docx_to_chunks: DOCX document → Markdown → chunks
    - test_mixed_document_batch: Multiple formats in one batch
"""
