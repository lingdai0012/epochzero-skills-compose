"""GitHub/GitLab connector via Git API.

Fetches documentation files from configured repositories.

Classes to implement:
    - GitHubConnector(SourceConnector):
        - Authenticates via GitHub token or GitHub App
        - Scans configured repos and path patterns (README.md, docs/**, ADR/**)
        - Fetches file content via API (avoids full clone)
        - Supports webhook-triggered sync on push events
        - Maps repo/path to team metadata
"""
