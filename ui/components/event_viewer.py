import streamlit as st

from ui.cache import get_pod_events


def render_event_viewer(
        namespace: str,
        pod_name: str,
):
    """
    Render pod events.
    """

    events = get_pod_events(
        namespace,
        pod_name,
    )

    if not events:

        st.info(
            "No events found."
        )

        return

    rows = []

    for event in events:

        rows.append(
            {
                "Time": event.get(
                    "lastTimestamp",
                    "-"
                )
                        or event.get(
                    "eventTime",
                    "-"
                ),
                "Type": event.get(
                    "type",
                    "-"
                ),
                "Reason": event.get(
                    "reason",
                    "-"
                ),
                "Object": event.get(
                    "involvedObject",
                    {},
                ).get(
                    "name",
                    "-"
                ),
                "Message": event.get(
                    "message",
                    "-"
                ),
            }
        )

    st.dataframe(
        rows,
        use_container_width=True,
        hide_index=True,
    )