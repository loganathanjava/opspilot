from models.openshift import ClusterSummary, NamespaceHealth
from services.openshift.namespaces import NamespaceService
from services.openshift.pods import PodService


class ClusterService:

    def __init__(self):
        self.namespace_service = NamespaceService()
        self.pod_service = PodService()

    def summary(self) -> ClusterSummary:
        """
        Returns overall cluster statistics.
        """

        namespaces = self.namespace_service.list_namespaces().get(
            "items",
            [],
        )

        stats = {
            "namespaces": len(namespaces),
            "pods": 0,
            "running": 0,
            "pending": 0,
            "failed": 0,
            "unhealthy": 0,
            "restarting": 0,
        }

        for ns in namespaces:

            namespace = ns["metadata"]["name"]

            pods = self.pod_service.list_pods(namespace)

            stats["pods"] += len(pods)

            for pod in pods:

                if pod.status == "Running":
                    stats["running"] += 1

                elif pod.status == "Pending":
                    stats["pending"] += 1

                elif pod.status == "Failed":
                    stats["failed"] += 1

                if pod.reason != pod.status:
                    stats["unhealthy"] += 1

                if pod.restart_count > 0:
                    stats["restarting"] += 1

        return ClusterSummary(
            namespaces=stats["namespaces"],
            pods=stats["pods"],
            running=stats["running"],
            pending=stats["pending"],
            failed=stats["failed"],
            unhealthy=stats["unhealthy"],
            restarting=stats["restarting"],
        )

    def namespace_health(self) -> list[NamespaceHealth]:
        """
        Returns health statistics for every namespace.
        """

        namespaces = self.namespace_service.list_namespaces().get(
            "items",
            [],
        )

        results: list[NamespaceHealth] = []

        for ns in namespaces:

            namespace = ns["metadata"]["name"]

            pods = self.pod_service.list_pods(namespace)

            running = 0
            pending = 0
            failed = 0
            unhealthy = 0

            for pod in pods:

                if pod.status == "Running":
                    running += 1

                elif pod.status == "Pending":
                    pending += 1

                elif pod.status == "Failed":
                    failed += 1

                if pod.reason != pod.status:
                    unhealthy += 1

            results.append(
                NamespaceHealth(
                    name=namespace,
                    pods=len(pods),
                    running=running,
                    pending=pending,
                    failed=failed,
                    unhealthy=unhealthy,
                )
            )

        results.sort(
            key=lambda x: (
                x.unhealthy,
                x.failed,
                x.pending,
            ),
            reverse=True,
        )

        return results