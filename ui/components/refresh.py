import streamlit as st


def render_refresh_button():
    """
    Render the refresh button.
    """

    if st.button("🔄 Refresh", use_container_width=True):
        st.cache_data.clear()
        st.rerun()