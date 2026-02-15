"""Tests for VersionManager in src/registry/version_manager.py.

Tests to implement:
    - test_initial_version: Returns "1.0.0"
    - test_bump_patch: content_update → 1.0.0 → 1.0.1
    - test_bump_minor: structural_change → 1.0.1 → 1.1.0
    - test_bump_major: hierarchy_change → 1.1.0 → 2.0.0
    - test_bump_minor_resets_patch: 1.2.3 → 1.3.0
    - test_bump_major_resets_all: 1.2.3 → 2.0.0
"""
