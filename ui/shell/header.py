import streamlit as st


def render_header():
    """
    Render application header.
    """

    left, right = st.columns([4, 1])

    with left:

        st.title("🚀 OpsPilot")

        st.caption(
            "AI Powered OpenShift Operations Console"
        )

    with right:

        st.success("🟢 Connected")