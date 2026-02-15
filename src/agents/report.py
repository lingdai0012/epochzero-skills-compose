"""Weekly metrics report generator.

Classes to implement:
    - WeeklyReportGenerator:
        Generates a weekly summary report of skill performance.

        Methods:
            - async generate(period: str = "7d") -> str
                Produces report with:
                - Total skills count by level
                - Total trigger count across all agents
                - Top performing skills (by trigger count and quality)
                - Needs attention (high correction rate, gap detections)
                - Pending updates (skills affected by source changes)
"""
