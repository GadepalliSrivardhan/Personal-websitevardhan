from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="Srivardhan Gadepalli Portfolio",
    page_icon=":briefcase:",
    layout="wide",
)

html_file = Path(__file__).with_name("index.html")

if not html_file.exists():
    st.error("index.html was not found in this repository.")
    st.stop()

html_content = html_file.read_text(encoding="utf-8")

# Render the existing portfolio exactly as authored.
components.html(html_content, height=5000, scrolling=True)
