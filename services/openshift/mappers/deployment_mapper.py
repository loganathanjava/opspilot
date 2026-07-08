from models.openshift import Deployment
from services.openshift.parsers import DeploymentParser


class DeploymentMapper:
    """
    Maps OpenShift Deployment API responses
    to Deployment domain models.
    """

    @staticmethod
    def from_api(item: dict) -> Deployment:

        metadata = item.get(
            "metadata",
            {},
        )

        return Deployment(
            name=metadata.get(
                "name",
                "",
            ),
            namespace=metadata.get(
                "namespace",
                "",
            ),
            ready=DeploymentParser.ready(
                item,
            ),
            available=DeploymentParser.available(
                item,
            ),
            replicas=DeploymentParser.replicas(
                item,
            ),
            strategy=DeploymentParser.strategy(
                item,
            ),
            age=DeploymentParser.age(
                item,
            ),
        )