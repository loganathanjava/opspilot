import streamlit as st

from ui.cache import get_pod_yaml


def render_yaml_viewer(
        namespace: str,
        pod_name: str,
):
    """
    Render Pod YAML.
    """

    with st.expander(
            "📄 Pod YAML",
            expanded=False,
    ):

        yaml_text = get_pod_yaml(
            namespace,
            pod_name,
        )

        st.code(
            yaml_text,
            language="yaml",
        )

        st.download_button(
            "⬇ Download YAML",
            yaml_text,
            file_name=f"{pod_name}.yaml",
            use_container_width=True,
        )