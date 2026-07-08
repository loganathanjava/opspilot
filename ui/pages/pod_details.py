import streamlit as st

from ui.cache import get_pod
from ui.components import (
    render_event_viewer,
    render_log_viewer,
    render_yaml_viewer,
)


def render_pod_details(
        namespace: str,
        pod_name: str,
):
    pod = get_pod(
        namespace,
        pod_name,
    )

    metadata = pod.get("metadata", {})
    spec = pod.get("spec", {})
    status = pod.get("status", {})

    containers = [
        c["name"]
        for c in spec.get(
            "containers",
            [],
        )
    ]

    overview_tab, logs_tab, events_tab, yaml_tab = st.tabs(
        [
            "📄 Overview",
            "📜 Logs",
            "📅 Events",
            "📄 YAML",
        ]
    )

    with overview_tab:

        st.subheader("Pod Overview")

        left, right = st.columns(2)

        with left:

            st.write("**Name**")
            st.write(metadata.get("name"))

            st.write("**Namespace**")
            st.write(metadata.get("namespace"))

            st.write("**Phase**")
            st.write(status.get("phase"))

            st.write("**Pod IP**")
            st.write(status.get("podIP", "-"))

        with right:

            st.write("**Node**")
            st.write(spec.get("nodeName", "-"))

            st.write("**Host IP**")
            st.write(status.get("hostIP", "-"))

            st.write("**QoS**")
            st.write(status.get("qosClass", "-"))

            st.write("**Service Account**")
            st.write(
                spec.get(
                    "serviceAccountName",
                    "-",
                )
            )

        st.divider()

        st.subheader("Containers")

        for container in containers:
            st.write(f"• **{container}**")

    with logs_tab:

        render_log_viewer(
            namespace,
            pod_name,
            containers,
        )

    with events_tab:

        render_event_viewer(
            namespace,
            pod_name,
        )

    with yaml_tab:

        render_yaml_viewer(
            namespace,
            pod_name,
        )