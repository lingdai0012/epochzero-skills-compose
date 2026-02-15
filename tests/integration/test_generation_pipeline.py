"""Integration tests for the skill generation pipeline.

Tests to implement:
    - test_aggregate_classify_plan: Classified chunks → aggregation → plan
    - test_plan_to_skill: Plan → generated SKILL.md
    - test_hierarchical_generation: Corporate → Department → Team ordering
    - test_dedup_against_parent: Department skill avoids corporate content
"""
