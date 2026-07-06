from ui.core.page import Page
from ui.features.dashboard.dashboard import render_dashboard


class DashboardPage(Page):

    def __init__(self):

        super().__init__(
            id="dashboard",
            title="Dashboard",
            icon="📊",
            description="Cluster overview",
            category="Home",
            order=1,
        )

    def render(self):

        render_dashboard()