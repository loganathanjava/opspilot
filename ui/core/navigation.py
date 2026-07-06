import streamlit as st

from ui.core.registry import PAGES


def render_navigation():
    """
    Render the application navigation.
    """

    labels = [
        f"{page.icon} {page.title}"
        for page in sorted(
            PAGES,
            key=lambda p: p.order,
        )
    ]

    selected = st.sidebar.radio(
        "Navigation",
        labels,
    )

    for page in PAGES:

        label = f"{page.icon} {page.title}"

        if label == selected:
            return page

    return PAGES[0]