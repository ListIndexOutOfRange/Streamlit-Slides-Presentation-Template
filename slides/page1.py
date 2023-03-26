import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.subheader("Basics : Slides and Headers")
    pad_l, center, pad_r = st.columns([1, 3, 1])
    with center:
        st.markdown("""
            - You can add as many slides as you want by creating python files inside the
                `slides/` folder (1 file per slide)
                - you can organize each python file as you like but **each file MUST have a
                  `main() -> None` function that will be called to display the slide's content.**
            - Slides will be displayed by sorting alphanumerically the name of python files
                inside the `slides/` folder
            - Header, subheader, and footer can be set within the `config.toml` file.
                - Of course, you are free to create your own title page without the `config.toml`
                  file.
        """)
        st.write("___")
        st.write(
            "**Please to refer to the [streamlit documentation](https://docs.streamlit.io/) to \
             format your pages.**"
        )
