"""Google Drive connector via Drive API v3.

Recursively scans configured folders and exports documents to Markdown.

Classes to implement:
    - GoogleDriveConnector(SourceConnector):
        - Authenticates via service account
        - Recursively scans root_folders by ID
        - Exports Google Docs/Sheets/Slides to appropriate formats
        - Downloads binary files (PDF, DOCX, PPTX)
        - Filters by file_types configuration
        - Maps folder location to department/team metadata
"""
