import streamlit as st


def render_page_header(
        title: str,
        description: str | None = None,
):
    """
    Render a consistent page header.

    Parameters
    ----------
    title:
        Page title.

    description:
        Optional page description.
    """

    st.title(title)

    if description:
        st.caption(description)

    st.divider()