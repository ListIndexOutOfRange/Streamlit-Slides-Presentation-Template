import streamlit as st
from . import CONFIG


def main() -> None:
    for _ in range(20):
        st.write("")
    st.header(CONFIG["header"])
    st.markdown("___")
    st.caption(CONFIG["subheader"])
