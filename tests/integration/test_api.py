"""Integration tests for FastAPI endpoints.

Tests to implement:
    - test_list_skills: GET /api/skills returns skill list
    - test_get_skill_detail: GET /api/skills/{name} returns detail
    - test_review_queue: GET /api/review/queue returns pending skills
    - test_approve_skill: POST /api/review/{name}/approve publishes skill
    - test_reject_skill: POST /api/review/{name}/reject with comments
    - test_skill_loader_endpoint: GET /api/v1/skills/load with department/team params
    - test_rbac_admin: Admin can access all endpoints
    - test_rbac_viewer: Viewer can only read
"""
