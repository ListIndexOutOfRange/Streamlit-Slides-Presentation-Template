import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.markdown("""
        <h2 class='st-ae st-af st-ag st-ah st-ai st-aj st-ak st-al st-am st-bf st-an st-ao st-ap
        st-aq st-ar st-as st-at st-au st-av st-aw st-ax st-ay st-bb st-b0 st-b1 st-b2 st-b3 st-b4
        st-b5 st-b6 st-b7' style='text-align: center; font-weight: 600;'>
        This should be enough to get you started. The remaining is only about learning Streamlit.
        </h2>
    """, unsafe_allow_html=True)
