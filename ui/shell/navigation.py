from ui.pages import PAGES
import streamlit as st


def render_navigation():

    labels = [
        f"{page.icon} {page.title}"
        for page in PAGES
    ]

    choice = st.sidebar.radio(
        "",
        labels,
    )

    return next(
        page
        for page in PAGES
        if f"{page.icon} {page.title}" == choice
    )