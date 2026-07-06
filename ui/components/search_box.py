import streamlit as st


def render_search_box(
        label: str = "Search",
        placeholder: str = "Type to search...",
) -> str:
    """
    Render a reusable search box.

    Returns
    -------
    str
        Search text.
    """

    return st.text_input(
        label,
        placeholder=placeholder,
    ).strip()