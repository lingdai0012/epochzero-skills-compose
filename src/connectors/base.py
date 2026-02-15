"""Abstract base class for all source connectors.

Classes to implement:
    - SourceConnector (ABC):
        Abstract interface that all connectors must implement.

        Methods:
            - async fetch_documents(since: Optional[datetime] = None) -> List[RawDocument]
                Fetch documents, optionally only those modified since a given timestamp.

            - async test_connection() -> bool
                Verify that the connector can reach its data source.

            - name: str (property)
                Unique identifier for this connector type.
"""
