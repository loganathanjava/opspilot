import streamlit as st


def render_namespace_explorer(namespaces):
    """
    Render namespace selector.
    """

    st.subheader("📁 Namespaces")

    search = st.text_input(
        "🔍 Search",
        placeholder="Namespace...",
    )

    filtered = [
        ns
        for ns in namespaces
        if search.lower() in ns.name.lower()
    ]

    options = [ns.name for ns in filtered]

    if not options:
        st.info("No namespaces found.")
        return None

    current = st.session_state.get(
        "selected_namespace",
        options[0],
    )

    if current not in options:
        current = options[0]

    selected = st.radio(
        "Select Namespace",
        options,
        index=options.index(current),
        label_visibility="collapsed",
    )

    st.session_state.selected_namespace = selected

    return selected