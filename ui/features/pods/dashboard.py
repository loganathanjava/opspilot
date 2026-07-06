import streamlit as st

from ui.cache import get_all_pods
from ui.components import render_page_header


def render_pods():
    """
    Render the Pods Explorer.
    """

    render_page_header(
        title="☸ Pods",
        description="Explore pods across the cluster",
    )

    pods = get_all_pods()

    st.write(f"Total Pods: **{len(pods)}**")

    rows = [
        {
            "Namespace": pod.namespace,
            "Name": pod.name,
            "Status": pod.status,
            "Ready": pod.ready,
            "Restarts": pod.restart_count,
            "Node": pod.node,
            "Age": pod.age,
        }
        for pod in pods
    ]

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True,
    )