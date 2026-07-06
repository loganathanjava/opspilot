import streamlit as st

from ui.cache import get_pod_logs


def render_logs(
        namespace: str,
        pod_name: str,
):
    """
    Render pod logs.
    """

    st.subheader("📜 Pod Logs")

    try:

        logs = get_pod_logs(
            namespace,
            pod_name,
        )

        st.download_button(
            "⬇ Download Logs",
            logs,
            file_name=f"{pod_name}.log",
            mime="text/plain",
        )

        st.code(
            logs,
            language="text",
            height=500,
        )

    except Exception as ex:

        st.error(str(ex))