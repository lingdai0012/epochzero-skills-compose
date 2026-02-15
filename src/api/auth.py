"""Role-based access control (RBAC).

Classes to implement:
    - RBAC roles:
        - admin: review_all, publish, reject, edit_taxonomy, manage_sources
        - department_reviewer: review_department, publish_department, suggest_edits (scoped to dept)
        - viewer: read_all

    - Functions:
        - get_current_user(request) -> User
        - require_role(role: str) -> Dependency
        - check_department_scope(user: User, department: str) -> bool
"""
