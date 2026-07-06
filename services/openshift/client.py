import httpx

from config.settings import settings
from services.openshift.exceptions import (
    OpenShiftAPIError,
    OpenShiftAuthenticationError,
    OpenShiftNotFound,
    OpenShiftPermissionDenied,
)


class OpenShiftClient:
    """
    Simple OpenShift REST client.
    """

    def __init__(self):

        self.base_url = settings.OPENSHIFT_API.rstrip("/")
        self.token = settings.OPENSHIFT_TOKEN.strip()

        self.client = httpx.Client(
            verify=settings.VERIFY_SSL,
            follow_redirects=True,
            timeout=30.0,
            headers={
                "Authorization": f"Bearer {self.token}",
                "Accept": "application/json",
            },
        )

    def get(
            self,
            path: str,
            params: dict | None = None,
    ):

        return self._request(
            "GET",
            path,
            params=params,
        )

    def post(
            self,
            path: str,
            json: dict | None = None,
    ):

        return self._request(
            "POST",
            path,
            json=json,
        )

    def put(
            self,
            path: str,
            json: dict | None = None,
    ):

        return self._request(
            "PUT",
            path,
            json=json,
        )

    def patch(
            self,
            path: str,
            json: dict | None = None,
    ):

        return self._request(
            "PATCH",
            path,
            json=json,
        )

    def delete(
            self,
            path: str,
    ):

        return self._request(
            "DELETE",
            path,
        )

    def _request(
            self,
            method: str,
            path: str,
            **kwargs,
    ):
        """
        Execute an HTTP request.
        """

        if not path.startswith("/"):
            path = "/" + path

        url = f"{self.base_url}{path}"

        print(f"{method} {url}")

        response = self.client.request(
            method,
            url,
            **kwargs,
        )

        print(f"Status: {response.status_code}")

        if response.status_code == 401:
            raise OpenShiftAuthenticationError(
                "Authentication failed."
            )

        if response.status_code == 403:
            raise OpenShiftPermissionDenied(
                "Permission denied."
            )

        if response.status_code == 404:
            raise OpenShiftNotFound(
                "Resource not found."
            )

        if response.status_code >= 400:
            raise OpenShiftAPIError(
                response.text
            )

        if not response.content:
            return None

        content_type = response.headers.get(
            "content-type",
            "",
        )

        if "application/json" in content_type:
            return response.json()

        return response.text