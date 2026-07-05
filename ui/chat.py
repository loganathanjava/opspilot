import streamlit as st

from services.agent_service import AgentService


def render_chat():

    st.title("🤖 OpsPilot")

    if "agent" not in st.session_state:
        st.session_state.agent = AgentService()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask OpsPilot...")

    if not prompt:
        return

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response
    with st.spinner("Thinking..."):

        response = st.session_state.agent.chat(prompt)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)