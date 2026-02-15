"""Tests for SkillFileWriter in src/generation/file_writer.py.

Tests to implement:
    - test_write_corporate_skill: Writes to skills/corporate/{name}/SKILL.md
    - test_write_department_skill: Writes to skills/departments/{dept}/{name}/SKILL.md
    - test_write_team_skill: Writes to skills/teams/{dept}/{team}/{name}/SKILL.md
    - test_write_reference_files: Creates references/ subdirectory with files
    - test_write_registry_json: Generates valid registry.json
    - test_overwrite_existing: Overwrites previous version
    - test_creates_directories: Creates parent directories if needed
"""
