from services.openshift.base import BaseService

import yaml


class PodYamlService(BaseService):
    """
    Service for retrieving pod YAML.
    """

    def get_yaml(
            self,
            namespace: str,
            pod_name: str,
    ) -> str:
        """
        Returns pod definition as YAML.
        """

        pod = self.client.get(
            f"/api/v1/namespaces/{namespace}/pods/{pod_name}"
        )

        return yaml.safe_dump(
            pod,
            sort_keys=False,
            default_flow_style=False,
        )