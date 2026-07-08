from ui.core.page import Page
from ui.features.pods.dashboard import render_pods


class PodsPage(Page):

    def __init__(self):

        super().__init__(
            id="pods",
            title="Pods",
            icon="☸",
            description="Explore pods across the cluster",
            category="Workloads",
            order=2,
        )

    def render(self):

        render_pods()