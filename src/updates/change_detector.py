"""Change detection across data source connectors.

Classes to implement:
    - ChangeDetector:
        Detects new, modified, and deleted documents across all connected sources.

        __init__(connectors: List[SourceConnector], state_store: StateStore)

        Methods:
            - async detect() -> ChangeReport
                For each connector:
                1. Fetch documents since last sync
                2. Compare content hashes against stored state
                3. Filter trivial edits (significance < 10%)
                4. Detect deletions (IDs present in state but missing from fetch)
                5. Update sync timestamps

    - StateStore:
        Persists last sync timestamps, document hashes, and content snapshots.

        Methods:
            - get_last_sync(connector_name: str) -> Optional[datetime]
            - get_hash(document_id: str) -> Optional[str]
            - get_content(document_id: str) -> Optional[str]
            - get_document_ids(connector_name: str) -> Set[str]
            - update_sync(connector_name: str, timestamp: datetime) -> None
"""
