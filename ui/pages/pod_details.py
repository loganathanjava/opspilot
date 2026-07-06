import streamlit as st

from ui.cache import get_pod


def render_pod_details(
        namespace: str,
        pod_name: str,
):
    """
    Render pod details.
    """

    pod = get_pod(
        namespace,
        pod_name,
    )

    metadata = pod.get("metadata", {})
    spec = pod.get("spec", {})
    status = pod.get("status", {})

    st.subheader("📄 Pod Overview")

    left, right = st.columns(2)

    with left:

        st.markdown("##### General")

        st.write("**Name**")
        st.write(metadata.get("name"))

        st.write("**Namespace**")
        st.write(metadata.get("namespace"))

        st.write("**Phase**")
        st.write(status.get("phase"))

        st.write("**Pod IP**")
        st.write(status.get("podIP", "-"))

    with right:

        st.markdown("##### Runtime")

        st.write("**Node**")
        st.write(spec.get("nodeName", "-"))

        st.write("**Host IP**")
        st.write(status.get("hostIP", "-"))

        st.write("**QoS Class**")
        st.write(status.get("qosClass", "-"))

        st.write("**Service Account**")
        st.write(
            spec.get(
                "serviceAccountName",
                "-",
            )
        )

    st.divider()

    st.subheader("📦 Containers")

    containers = spec.get(
        "containers",
        [],
    )

    for container in containers:

        st.write(
            f"• **{container['name']}**"
        )

    st.divider()

    st.subheader("🛠 Diagnostics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.button(
            "📜 Logs",
            disabled=True,
            use_container_width=True,
        )

    with c2:
        st.button(
            "📅 Events",
            disabled=True,
            use_container_width=True,
        )

    with c3:
        st.button(
            "📄 YAML",
            disabled=True,
            use_container_width=True,
        )