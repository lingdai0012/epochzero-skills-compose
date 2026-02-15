"""Confluence connector via REST API v2.

Fetches pages from configured Confluence spaces, converting content to Markdown.

Classes to implement:
    - ConfluenceConnector(SourceConnector):
        - Authenticates via OAuth2 or API token
        - Fetches pages from configured spaces (BRAND, INVEST, ENG, COMPLY, etc.)
        - Excludes pages with specified labels (draft, archived)
        - Converts Confluence storage format to Markdown
        - Supports incremental fetch (since parameter)
"""
