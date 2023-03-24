import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    _, center, _ = st.columns([1, 2.2, 1])
    with center:
        st.info("""
            **This should be enough to get you started. The remaining is only about learning \
            Streamlit.**
        """)
