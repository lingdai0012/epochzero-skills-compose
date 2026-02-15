"""QA pipeline orchestrator and report generator.

Classes to implement:
    - QAPipeline:
        Orchestrates all QA checks and determines publish/review/reject decision.

        Methods:
            - async check(skill: GeneratedSkill) -> QAReport
                Run structural, content, and security checks
                Aggregate results into QAReport with overall decision

            - _determine_decision(results: List[QACheck]) -> str
                Apply thresholds from qa_thresholds.yaml:
                - auto_publish: structural all_pass, content_accuracy >= 0.9, security all_pass
                - needs_review: structural all_pass, content_accuracy >= 0.7, security all_pass
                - rejected: any fail

    - QAReportGenerator:
        Generates human-readable Markdown QA reports.

        Methods:
            - generate_report(qa_report: QAReport) -> str
"""
