from services.openshift.utils import KubernetesUtils


class DeploymentParser:
    """
    Parses Deployment API responses.
    """

    @staticmethod
    def ready(item: dict) -> str:

        status = item.get(
            "status",
            {},
        )

        ready = status.get(
            "readyReplicas",
            0,
        )

        replicas = status.get(
            "replicas",
            0,
        )

        return f"{ready}/{replicas}"

    @staticmethod
    def available(item: dict) -> int:

        return item.get(
            "status",
            {},
        ).get(
            "availableReplicas",
            0,
        )

    @staticmethod
    def replicas(item: dict) -> int:

        return item.get(
            "spec",
            {},
        ).get(
            "replicas",
            0,
        )

    @staticmethod
    def strategy(item: dict) -> str:

        return item.get(
            "spec",
            {},
        ).get(
            "strategy",
            {},
        ).get(
            "type",
            "-",
        )

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