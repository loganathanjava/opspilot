from services.openshift.client import OpenShiftClient


class BaseService:

    def __init__(self):
        self.client = OpenShiftClient()