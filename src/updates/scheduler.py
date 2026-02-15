"""Scheduling for periodic sync and webhook-triggered updates.

Classes to implement:
    - SyncScheduler:
        Manages cron-based and webhook-triggered sync schedules.

        Methods:
            - load_schedule(config_path: str) -> None
                Load schedule.yaml:
                  confluence: cron "0 2 * * *" (daily at 2 AM)
                  github: webhook on push to main
                  gdrive: cron "0 3 * * 1" (weekly Monday 3 AM)

            - start() -> None
                Start the scheduler loop

            - trigger(connector_name: str) -> None
                Manually trigger a sync for a specific connector

            - handle_webhook(event: dict) -> None
                Process incoming webhook events (e.g., GitHub push)
"""
