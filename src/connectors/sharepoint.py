"""SharePoint/OneDrive connector via Microsoft Graph API.

Similar to Google Drive connector but using Microsoft Graph API.

Classes to implement:
    - SharePointConnector(SourceConnector):
        - Authenticates via Microsoft Graph API (OAuth2)
        - Scans configured SharePoint sites and document libraries
        - Downloads and converts documents
        - Maps site/library location to department/team metadata
"""
