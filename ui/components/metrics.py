import streamlit as st


def render_cluster_metrics(summary):
    """
    Render the cluster summary metric cards.
    """

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🟢 Running Pods", summary.running)
        st.metric("🟡 Pending Pods", summary.pending)

    with col2:
        st.metric("🔴 Unhealthy Pods", summary.unhealthy)
        st.metric("🔄 Restarting Pods", summary.restarting)

    with col3:
        st.metric("📦 Total Pods", summary.pods)
        st.metric("📁 Namespaces", summary.namespaces)