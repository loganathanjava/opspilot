import streamlit as st


def render_metric_card(
        title: str,
        value,
        help: str | None = None,
):
    """
    Render a standardized metric card.

    Parameters
    ----------
    title:
        Metric title.

    value:
        Metric value.

    help:
        Optional tooltip.
    """

    st.metric(
        label=title,
        value=value,
        help=help,
    )