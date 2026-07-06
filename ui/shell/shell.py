from ui.shell.header import render_header
from ui.shell.navigation import render_navigation


def render_shell():

    render_header()

    page = render_navigation()

    page.render()