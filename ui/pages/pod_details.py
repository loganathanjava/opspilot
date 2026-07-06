import streamlit as st

from ui.cache import get_pod
from ui.components import (
    render_log_viewer,
    render_yaml_viewer,
)


def render_pod_details(
        namespace: str,
        pod_name: str,
):
    """
    Render pod details.
    """

    pod = get_pod(
        namespace,
        pod_name,
    )

    metadata = pod.get("metadata", {})
    spec = pod.get("spec", {})
    status = pod.get("status", {})

    containers = [
        container["name"]
        for container in spec.get(
            "containers",
            [],
        )
    ]

    overview_tab, logs_tab, yaml_tab = st.tabs(
        [
            "📄 Overview",
            "📜 Logs",
            "📄 YAML",
        ]
    )

    # ---------------------------------------------------------
    # Overview
    # ---------------------------------------------------------

    with overview_tab:

        st.subheader("Pod Overview")

        left, right = st.columns(2)

        with left:

            st.markdown("##### General")

            st.write("**Name**")
            st.write(metadata.get("name"))

            st.write("**Namespace**")
            st.write(metadata.get("namespace"))

            st.write("**Phase**")
            st.write(status.get("phase"))

            st.write("**Pod IP**")
            st.write(status.get("podIP", "-"))

        with right:

            st.markdown("##### Runtime")

            st.write("**Node**")
            st.write(spec.get("nodeName", "-"))

            st.write("**Host IP**")
            st.write(status.get("hostIP", "-"))

            st.write("**QoS Class**")
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

        if containers:

            for container in containers:

                st.write(f"• **{container}**")

        else:

            st.info("No containers found.")

    # ---------------------------------------------------------
    # Logs
    # ---------------------------------------------------------

    with logs_tab:

        render_log_viewer(
            namespace=namespace,
            pod_name=pod_name,
            containers=containers,
        )

    # ---------------------------------------------------------
    # YAML
    # ---------------------------------------------------------

    with yaml_tab:

        render_yaml_viewer(
            namespace=namespace,
            pod_name=pod_name,
        )