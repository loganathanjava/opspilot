import streamlit as st


def render_pod_table(
        pods,
):
    """
    Render pod table.
    """

    rows = []

    for pod in pods:

        rows.append(
            {
                "Namespace": pod.namespace,
                "Name": pod.name,
                "Ready": pod.ready,
                "Status": pod.status,
                "Restarts": pod.restart_count,
                "Node": pod.node,
                "Age": pod.age,
            }
        )

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True,
    )