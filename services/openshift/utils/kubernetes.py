from datetime import datetime, timezone


class KubernetesUtils:
    """
    Common Kubernetes helper methods.
    """

    @staticmethod
    def calculate_age(timestamp: str | None) -> str:
        """
        Convert Kubernetes creationTimestamp into
        a human-readable age.
        """

        if not timestamp:
            return "-"

        created = datetime.fromisoformat(
            timestamp.replace(
                "Z",
                "+00:00",
            )
        )

        delta = (
                datetime.now(timezone.utc)
                - created
        )

        days = delta.days

        if days > 0:
            return f"{days}d"

        hours = delta.seconds // 3600

        if hours > 0:
            return f"{hours}h"

        minutes = delta.seconds // 60

        return f"{minutes}m"