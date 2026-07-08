from services.openshift.utils import KubernetesUtils


class PodParser:
    """
    Parses Pod API responses.
    """

    @staticmethod
    def ready(item: dict) -> str:

        statuses = item.get(
            "status",
            {},
        ).get(
            "containerStatuses",
            [],
        )

        ready = sum(
            1
            for status in statuses
            if status.get("ready")
        )

        return f"{ready}/{len(statuses)}"

    @staticmethod
    def status(item: dict) -> str:

        return item.get(
            "status",
            {},
        ).get(
            "phase",
            "Unknown",
        )

    @staticmethod
    def restart_count(item: dict) -> int:

        statuses = item.get(
            "status",
            {},
        ).get(
            "containerStatuses",
            [],
        )

        return sum(
            status.get(
                "restartCount",
                0,
            )
            for status in statuses
        )

    @staticmethod
    def reason(item: dict) -> str:

        statuses = item.get(
            "status",
            {},
        ).get(
            "containerStatuses",
            [],
        )

        for status in statuses:

            waiting = status.get(
                "state",
                {},
            ).get(
                "waiting",
            )

            if waiting:

                return waiting.get(
                    "reason",
                    "Waiting",
                )

        return PodParser.status(item)

    @staticmethod
    def age(item: dict) -> str:

        timestamp = item.get(
            "metadata",
            {},
        ).get(
            "creationTimestamp",
        )

        return KubernetesUtils.calculate_age(
            timestamp,
        )

    @staticmethod
    def is_unhealthy(item: dict) -> bool:

        if PodParser.status(item) != "Running":
            return True

        statuses = item.get(
            "status",
            {},
        ).get(
            "containerStatuses",
            [],
        )

        for status in statuses:

            waiting = status.get(
                "state",
                {},
            ).get(
                "waiting",
            )

            if waiting:
                return True

            if status.get(
                    "restartCount",
                    0,
            ) > 0:
                return True

        return False