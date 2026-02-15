"""Format converters to normalize documents into Markdown.

Functions/classes to implement:
    - convert_pdf(path: str) -> str
        PDF → Markdown via pymupdf or docling

    - convert_docx(path: str) -> str
        DOCX → Markdown via pandoc or python-docx

    - convert_html(content: str) -> str
        HTML → Markdown via markdownify or trafilatura

    - convert_plaintext(content: str) -> str
        Plain text passthrough with minimal formatting

    - convert_code(content: str, language: str) -> str
        Code files → Markdown with language-tagged fenced code blocks

    - convert_document(path_or_content: str, content_type: str) -> str
        Dispatcher that routes to the appropriate converter based on content type
"""
