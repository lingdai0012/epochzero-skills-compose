"""Skill performance metrics computation.

Classes to implement:
    - SkillMetrics:
        Computes key metrics per skill over a configurable time window.

        Methods:
            - compute(skill_name: str, window: str = "30d") -> dict
                Returns:
                - Usage: trigger_count, trigger_rate, false_positive_rate
                - Quality: avg_output_quality, user_correction_rate
                - Freshness: days_since_update, source_docs_changed_since
                - Efficiency: avg_tokens_in_context, load_time_ms
"""
