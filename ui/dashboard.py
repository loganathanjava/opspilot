import streamlit as st

from ui.cache import (
    get_cluster_summary,
    get_namespace_health,
)
from ui.components.metrics import render_cluster_metrics
from ui.components.namespace_explorer import render_namespace_explorer
from ui.components.refresh import render_refresh_button
from ui.pages.namespace_details import render_namespace_details


def render_dashboard():
    """
    Render the OpenShift dashboard.
    """

    # ------------------------------------------------------------------
    # Header
    # ------------------------------------------------------------------

    header, refresh = st.columns([6, 1])

    with header:
        st.title("📊 OpenShift Dashboard")

    with refresh:
        render_refresh_button()

    # ------------------------------------------------------------------
    # Cluster Summary
    # ------------------------------------------------------------------

    summary = get_cluster_summary()

    render_cluster_metrics(summary)

    st.divider()

    # ------------------------------------------------------------------
    # Namespace Explorer + Details
    # ------------------------------------------------------------------

    namespaces = get_namespace_health()

    left, right = st.columns([1, 2], gap="large")

    with left:

        selected_namespace = render_namespace_explorer(
            namespaces
        )

    with right:

        if selected_namespace:

            render_namespace_details(
                selected_namespace
            )

        else:

            st.info(
                "Select a namespace to view its details."
            )