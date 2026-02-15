"""Tests for format converters in src/ingestion/format_converters.py.

Tests to implement:
    - test_convert_pdf: PDF → Markdown conversion
    - test_convert_docx: DOCX → Markdown conversion
    - test_convert_html: HTML → Markdown conversion
    - test_convert_plaintext: Plain text passthrough
    - test_convert_code: Code → Markdown with language tags
    - test_convert_document_dispatcher: Routes to correct converter
    - test_unsupported_format: Raises appropriate error
"""
