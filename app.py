import streamlit as st

from ui.sidebar import render_sidebar
from ui.dashboard import render_dashboard
from ui.chat import render_chat


st.set_page_config(
    page_title="OpsPilot",
    page_icon="🤖",
    layout="wide",
)

# Sidebar
render_sidebar()

# Dashboard
render_dashboard()

st.divider()

# AI Chat
render_chat()