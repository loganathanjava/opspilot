import streamlit as st

from ui.cache import (
    get_cluster_summary,
    get_namespace_health,
)
from ui.components import (
    render_metric_card,
    render_page_header,
)
from ui.pages.namespace_details import render_namespace_details


def render_dashboard():
    """
    Render the main dashboard.
    """

    render_page_header(
        title="📊 Dashboard",
        description="Cluster overview and health summary",
    )

    summary = get_cluster_summary()

    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        render_metric_card(
            "Namespaces",
            summary.namespaces,
        )

    with col2:
        render_metric_card(
            "Pods",
            summary.pods,
        )

    with col3:
        render_metric_card(
            "Running",
            summary.running,
        )

    with col4:
        render_metric_card(
            "Pending",
            summary.pending,
        )

    with col5:
        render_metric_card(
            "Failed",
            summary.failed,
        )

    with col6:
        render_metric_card(
            "Unhealthy",
            summary.unhealthy,
        )

    st.subheader("Namespace Health")

    namespace_health = get_namespace_health()

    if not namespace_health:
        st.info("No namespaces found.")
        return

    namespace_names = [ns.name for ns in namespace_health]

    selected_namespace = st.selectbox(
        "Select Namespace",
        namespace_names,
    )

    selected_health = next(
        ns
        for ns in namespace_health
        if ns.name == selected_namespace
    )

    st.dataframe(
        [
            {
                "Namespace": selected_health.name,
                "Pods": selected_health.pods,
                "Running": selected_health.running,
                "Pending": selected_health.pending,
                "Failed": selected_health.failed,
                "Unhealthy": selected_health.unhealthy,
            }
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.divider()

    render_namespace_details(
        selected_namespace,
    )