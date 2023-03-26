import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.subheader("Nested layout")
    _, center, _ = st.columns([1, 3, 1])
    with center:
        st.write("""
            Streamlit prevents the use of nested columns and expanders.
            I use the [streamlit-nested-layout](https://github.com/joy13975/streamlit-nested-layout)
            monkey patch to circumvent this limitations. It seems to work flawlessly in most cases,
            but sometimes occurs errors. You can disable the use of nested layouts using the
            appropriate option in the  `config.toml` file.
        """)
