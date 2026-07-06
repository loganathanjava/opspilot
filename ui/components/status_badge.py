import streamlit as st


_STATUS = {
    "Running": "🟢 Running",
    "Succeeded": "🟢 Succeeded",
    "Completed": "🟢 Completed",

    "Pending": "🟡 Pending",

    "Failed": "🔴 Failed",
    "CrashLoopBackOff": "🔴 CrashLoopBackOff",
    "ImagePullBackOff": "🔴 ImagePullBackOff",
    "ErrImagePull": "🔴 ErrImagePull",
    "CreateContainerConfigError": "🔴 ConfigError",
    "CreateContainerError": "🔴 ContainerError",

    "Unknown": "⚪ Unknown",
}


def render_status_badge(
        status: str,
):
    """
    Render a standardized status badge.
    """

    st.write(
        _STATUS.get(
            status,
            f"🔵 {status}",
        )
    )