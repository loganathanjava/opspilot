import streamlit as st

from ui.cache import get_deployments
from ui.components import (
    render_deployment_table,
    render_page_header,
)


def render_deployments():
    """
    Render deployment explorer.
    """

    render_page_header(
        "📦 Deployments",
        "Browse deployments across the cluster.",
    )

    deployments = get_deployments()

    selected = render_deployment_table(
        deployments,
    )

    if not selected:
        return

    namespace, deployment = selected

    st.success(
        f"Selected Deployment: {namespace}/{deployment}"
    )