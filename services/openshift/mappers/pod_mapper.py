from models.openshift import Pod
from services.openshift.parsers import PodParser


class PodMapper:
    """
    Maps OpenShift API responses to Pod domain models.
    """

    @staticmethod
    def from_api(item: dict, namespace: str) -> Pod:
        """
        Convert an OpenShift Pod API response into a Pod model.
        """

        return Pod(
            name=item["metadata"]["name"],
            namespace=namespace,
            ready=PodParser.ready(item),
            status=PodParser.status(item),
            restart_count=PodParser.restart_count(item),
            reason=PodParser.reason(item),
            node=item.get("spec", {}).get("nodeName"),
            age=PodParser.age(item),
        )