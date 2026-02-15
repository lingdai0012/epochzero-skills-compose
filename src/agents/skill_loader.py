"""Skill loader for AI agents.

Classes to implement:
    - SkillLoader:
        Loads the appropriate skills for an agent based on its department/team identity.

        Methods:
            - load_for_agent(agent_id: str, department: str, team: str, context?: str) -> LoadedSkillSet
                Layer 1: Corporate skills (always loaded, metadata only initially)
                Layer 2: Department skills (scoped to agent's department)
                Layer 3: Team skills (scoped to agent's team)
                Apply progressive disclosure: sort by priority, truncate if context limited
"""
