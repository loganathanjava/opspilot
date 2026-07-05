import pandas as pd
import streamlit as st


def _health(unhealthy: int, pending: int, failed: int) -> str:
    """
    Returns a health indicator for a namespace.
    """

    if unhealthy > 0 or failed > 0:
        return "🔴 Critical"

    if pending > 0:
        return "🟡 Warning"

    return "🟢 Healthy"


def render_namespace_table(namespaces):
    """
    Render the namespace health table.
    """

    st.subheader("📁 Namespace Health")

    search = st.text_input(
        "🔍 Search Namespace",
        placeholder="Search namespace...",
    )

    rows = []

    for ns in namespaces:

        if search and search.lower() not in ns.name.lower():
            continue

        rows.append(
            {
                "Health": _health(
                    ns.unhealthy,
                    ns.pending,
                    ns.failed,
                ),
                "Namespace": ns.name,
                "Pods": ns.pods,
                "Running": ns.running,
                "Pending": ns.pending,
                "Failed": ns.failed,
                "Unhealthy": ns.unhealthy,
            }
        )

    df = pd.DataFrame(rows)

    st.dataframe(
        df,
        hide_index=True,
        use_container_width=True,
        height=450,
    )