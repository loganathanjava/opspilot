import streamlit as st

from ui.chat import render_chat
from ui.core import render_shell


st.set_page_config(
    page_title="OpsPilot",
    page_icon="🚀",
    layout="wide",
)

render_shell()

st.divider()

render_chat()