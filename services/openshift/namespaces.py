from services.openshift.client import OpenShiftClient


class NamespaceService:

    def __init__(self):

        self.client = OpenShiftClient()

    def list_namespaces(self):

        return self.client.get("/api/v1/namespaces")