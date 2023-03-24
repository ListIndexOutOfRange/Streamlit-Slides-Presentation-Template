import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.subheader("Displaying image")
    pad_l, center, pad_r = st.columns([1, 3, 1])
    with center:
        st.write("You can display image with instructions alike:")
        st.code('st.image("./assets/ae.png", use_column_width=True)')
        st.image("./assets/ae.png", use_column_width=True)
        st.write("___")
        st.write(
            "**Please to refer to the [streamlit documentation](https://docs.streamlit.io/) to \
             format your pages.**"
        )
