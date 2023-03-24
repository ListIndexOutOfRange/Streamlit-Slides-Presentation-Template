import streamlit as st
import numpy as np
import plotly.graph_objects as go


def surface_plot() -> go.Figure:
    x = np.linspace(-8, 8, 50)
    y = np.linspace(-8, 8, 50)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X ** 2 + Y ** 2) + 1e-9
    Z = np.sin(R) / R
    fig = go.Figure(data=[go.Surface(z=Z, colorscale="jet")])
    fig.update_layout(margin=dict(l=20, r=20, b=20, t=20), autosize=True)
    return fig


def main() -> None:
    st.header("Quick how to ?")
    st.write("___")
    st.subheader("Interactive plot")
    _, center, _ = st.columns([1, 3, 1])
    with center:
        st.markdown("""
            You can create interactive plot using Plotly. I recommand creating a separated \
            function that returns a go.Figure() object, then calling:
        """)
        st.code("st.plotly_chart(fig, use_container_width=True)")
        fig = surface_plot()
        st.plotly_chart(fig, use_container_width=True)
