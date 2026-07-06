from ui.features.dashboard.page import DashboardPage

PAGES = [
    DashboardPage(),
]


def get_page(page_id: str):
    """
    Returns a page by id.
    """

    for page in PAGES:

        if page.id == page_id:
            return page

    return None