"""Manual file connector for Phase 1 MVP.

Scans a local directory for supported file types and loads them as RawDocuments.
Metadata is read from sidecar .meta.yaml files alongside each document.

Classes to implement:
    - ManualFileConnector(SourceConnector):
        Methods:
            - fetch_documents(since) -> List[RawDocument]
                Scan directory for supported files (.pdf, .docx, .html, .md, .txt, .py)
                Load sidecar .meta.yaml for each file to populate DocumentMetadata

            - test_connection() -> bool
                Check that the configured directory exists and is readable
"""
