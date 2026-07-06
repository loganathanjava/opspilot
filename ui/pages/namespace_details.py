import streamlit as st

from ui.cache import (
    get_namespace_summary,
    get_pods,
)
from ui.components.pod_table import render_pod_table
from ui.pages.pod_details import render_pod_details


def render_namespace_details(namespace: str):
    """
    Render namespace details.
    """

    st.subheader(f"📁 Namespace : {namespace}")

    summary = get_namespace_summary(namespace)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Deployments", summary["deployments"])
    c2.metric("Services", summary["services"])
    c3.metric("PVCs", summary["pvcs"])
    c4.metric("Events", summary["events"])

    st.divider()

    pods = get_pods(namespace)

    left, right = st.columns([1, 2], gap="large")

    with left:

        selected_pod = render_pod_table(pods)

    with right:

        if selected_pod:

            render_pod_details(
                namespace,
                selected_pod,
            )

        else:

            st.info("Select a pod.")