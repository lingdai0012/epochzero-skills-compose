"""Public website scraper using Playwright.

Scrapes configured public web pages and converts to Markdown.

Classes to implement:
    - WebScraperConnector(SourceConnector):
        - Uses Playwright for JavaScript-rendered pages
        - Crawls configured URLs with depth limits
        - Extracts main content (strips nav, footer, ads)
        - Converts HTML to Markdown
        - Respects robots.txt and rate limits
"""
