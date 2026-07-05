import streamlit as st

from ui.cache import get_namespace_summary


def render_namespace_details(namespace: str):
    """
    Render namespace summary cards.
    """

    st.subheader(f"📁 Namespace : {namespace}")

    summary = get_namespace_summary(namespace)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Deployments",
        summary["deployments"],
    )

    col2.metric(
        "Services",
        summary["services"],
    )

    col3.metric(
        "PVCs",
        summary["pvcs"],
    )

    col4.metric(
        "Events",
        summary["events"],
    )