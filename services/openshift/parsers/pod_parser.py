from datetime import datetime, timezone


class PodParser:
    """
    Utility methods for extracting pod information from the
    OpenShift/Kubernetes API response.
    """

    @staticmethod
    def container_statuses(item: dict) -> list:
        return item.get("status", {}).get("containerStatuses", [])

    @classmethod
    def ready(cls, item: dict) -> str:
        statuses = cls.container_statuses(item)

        ready = sum(
            1 for c in statuses
            if c.get("ready")
        )

        return f"{ready}/{len(statuses)}"

    @classmethod
    def restart_count(cls, item: dict) -> int:
        statuses = cls.container_statuses(item)

        return sum(
            c.get("restartCount", 0)
            for c in statuses
        )

    @staticmethod
    def status(item: dict) -> str:
        return item.get("status", {}).get("phase", "Unknown")

    @classmethod
    def reason(cls, item: dict) -> str:
        """
        Return the most meaningful reason for the pod state.
        """

        # Waiting reason (CrashLoopBackOff, ImagePullBackOff...)
        for status in cls.container_statuses(item):
            waiting = (
                status.get("state", {})
                .get("waiting")
            )

            if waiting:
                return waiting.get("reason", "Unknown")

        # Pod-level reason (Evicted, etc.)
        reason = item.get("status", {}).get("reason")

        if reason:
            return reason

        return cls.status(item)

    @staticmethod
    def age(item: dict) -> str:
        """
        Returns pod age in Kubernetes style.
        Example:
            35s
            8m
            2h
            3d
        """

        created = (
            item.get("metadata", {})
            .get("creationTimestamp")
        )

        if not created:
            return "-"

        created_dt = datetime.fromisoformat(
            created.replace("Z", "+00:00")
        )

        now = datetime.now(timezone.utc)

        delta = now - created_dt

        seconds = int(delta.total_seconds())

        if seconds < 60:
            return f"{seconds}s"

        minutes = seconds // 60

        if minutes < 60:
            return f"{minutes}m"

        hours = minutes // 60

        if hours < 24:
            return f"{hours}h"

        days = hours // 24

        return f"{days}d"

    @classmethod
    def is_unhealthy(cls, item: dict) -> bool:
        """
        Determines whether the pod should be considered unhealthy.
        """

        if cls.restart_count(item) > 0:
            return True

        unhealthy_reasons = {
            "CrashLoopBackOff",
            "ImagePullBackOff",
            "ErrImagePull",
            "CreateContainerConfigError",
            "CreateContainerError",
            "Evicted",
        }

        if cls.reason(item) in unhealthy_reasons:
            return True

        return False