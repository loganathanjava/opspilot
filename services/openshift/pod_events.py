from services.openshift.base import BaseService


class PodEventsService(BaseService):
    """
    Service for retrieving pod events.
    """

    def get_events(
            self,
            namespace: str,
            pod_name: str,
    ) -> list[dict]:
        """
        Returns events for a pod.
        """

        response = self.client.get(
            "/api/v1/namespaces/"
            f"{namespace}/events",
            params={
                "fieldSelector": (
                    f"involvedObject.name={pod_name}"
                )
            },
        )

        return response.get(
            "items",
            [],
        )