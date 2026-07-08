from ui.core.page import Page
from ui.features.deployments.deployments import (
    render_deployments,
)


class DeploymentsPage(Page):

    def __init__(self):

        super().__init__(
            id="deployments",
            title="Deployments",
            icon="📦",
            description="Browse deployments",
            category="Workloads",
            order=3,
        )

    def render(self):

        render_deployments()