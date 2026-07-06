from ui.shell.header import render_header
from ui.core.navigation import render_navigation


def render_shell():
    """
    Render the application shell.
    """

    render_header()

    page = render_navigation()

    page.render()