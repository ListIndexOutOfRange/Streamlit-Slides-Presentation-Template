import streamlit as st


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.subheader("Writing equations")
    _, center, _ = st.columns([1, 3, 1])
    with center:
        st.markdown("You can write Latex code with instructions alike:")
        st.code(r"""
    st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
''')
        """)
        st.latex(r'''
            a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
            \sum_{k=0}^{n-1} ar^k =
            a \left(\frac{1-r^{n}}{1-r}\right)
        ''')
        st.write("___")
        st.write(
            "**Please to refer to the [streamlit documentation](https://docs.streamlit.io/) to \
             format your pages.**"
        )
