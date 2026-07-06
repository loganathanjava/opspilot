import streamlit as st

from ui.cache import get_pod_logs


def render_log_viewer(
        namespace: str,
        pod_name: str,
        containers: list[str],
):
    """
    Render pod logs.
    """

    st.subheader("📜 Logs")

    if not containers:
        st.info("No containers found.")
        return

    if len(containers) == 1:
        container = containers[0]
        st.caption(f"Container: **{container}**")
    else:
        container = st.selectbox(
            "Container",
            containers,
        )

    col1, col2 = st.columns([1, 1])

    with col1:

        previous = st.checkbox(
            "Previous Logs",
            value=False,
        )

    with col2:

        tail_lines = st.selectbox(
            "Tail Lines",
            [100, 200, 500, 1000],
            index=2,
        )

    try:

        logs = get_pod_logs(
            namespace,
            pod_name,
            container,
            previous,
            tail_lines,
        )

        st.code(
            logs,
            language="text",
        )

        st.download_button(
            "⬇ Download Logs",
            logs,
            file_name=f"{pod_name}.log",
            use_container_width=True,
        )

    except Exception as ex:

        st.error(str(ex))