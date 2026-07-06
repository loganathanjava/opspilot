import streamlit as st


def _status_icon(status: str, reason: str) -> str:
    """
    Return a colored icon for pod health.
    """

    if status == "Running":
        return "🟢"

    if status == "Pending":
        return "🟡"

    if status == "Succeeded":
        return "🔵"

    if status == "Failed":
        return "🔴"

    if "CrashLoopBackOff" in reason:
        return "🔴"

    return "⚪"


def render_pod_table(pods):
    """
    Render pod explorer.
    """

    st.subheader("📦 Pods")

    search = st.text_input(
        "🔍 Search Pods",
        placeholder="Pod name...",
    )

    filtered = []

    for pod in pods:

        if search and search.lower() not in pod.name.lower():
            continue

        filtered.append(pod)

    if not filtered:

        st.info("No pods found.")

        return None

    pod_map = {
        f"{_status_icon(p.status, p.reason)} {p.name}": p.name
        for p in filtered
    }

    labels = list(pod_map.keys())

    current = st.session_state.get(
        "selected_pod",
        pod_map[labels[0]],
    )

    index = 0

    for i, label in enumerate(labels):

        if pod_map[label] == current:
            index = i
            break

    selected = st.radio(
        "Select Pod",
        labels,
        index=index,
        label_visibility="collapsed",
    )

    pod_name = pod_map[selected]

    st.session_state.selected_pod = pod_name

    return pod_name