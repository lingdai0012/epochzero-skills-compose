"""Shared utility functions.

Functions to implement:
    - hash_content(content: str) -> str
        Hash document content for change detection

    - count_tokens(text: str, model: str) -> int
        Count tokens for a given text and model

    - parse_markdown_headings(content: str) -> List[Section]
        Parse Markdown into heading-based sections with hierarchy

    - parse_yaml_frontmatter(content: str) -> Tuple[dict, str]
        Extract YAML frontmatter from SKILL.md content

    - render_yaml_frontmatter(metadata: dict) -> str
        Render metadata dict as YAML frontmatter block

    - truncate_to_token_limit(text: str, max_tokens: int) -> str
        Truncate text to fit within a token budget
"""
