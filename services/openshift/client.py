import httpx

from config.settings import settings


class OpenShiftClient:

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

    def get(self, path: str):

        if not path.startswith("/"):
            path = "/" + path

        url = f"{self.base_url}{path}"

        print(f"GET {url}")

        response = self.client.get(url)

        print(f"Status: {response.status_code}")

        if response.status_code >= 400:
            print(response.text)

        response.raise_for_status()

        return response.json()