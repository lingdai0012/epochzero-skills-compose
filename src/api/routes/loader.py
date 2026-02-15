"""Agent skill loading endpoint.

Endpoints to implement:
    - GET /api/v1/skills/load?department=X&team=Y
        Returns skills for an agent's identity:
        { metadata: [...], skills: { "corporate/glossary": "...", ... } }
        Loads Corporate + Department + Team skills with progressive disclosure
"""
