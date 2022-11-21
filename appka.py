import pandas as pd
import plotly.express as px
import streamlit as st


def app():
    st.title(" Dashboard")
    # st.text("muzes sem zkusit neco nahrat, vytvorime")
    # vstup 1: výběr datové sady
    data_file_path = st.file_uploader("Soubor k nahrani")

    if data_file_path is None:
        st.warning("No data file uploaded")
        return

    # read data if user uploads a file
    data = pd.read_csv(data_file_path)
    # seek back to position 0 after reading
    data_file_path.seek(0)

    # vstup 2: výběr parametrů scatter matrix
    dimensions = st.multiselect("Scatter matrix dimensions", list(data.columns), default=list(data.columns))
    color = st.selectbox("Color", data.columns)

    opacity = st.number_input('Opacity')
    # opacity = st.slider("Opacity", 0.0, 1.0, 0.5)
    # number = st.number_input('Insert a number')

    # scatter matrix plat
    st.write(px.scatter_matrix(data, dimensions=dimensions, color=color, opacity=opacity))

    # výběr sloupce pro zobrazení rozdělení dat
    interesting_column = st.selectbox("Interesting column", data.columns)
    # výběr funkce pro zobrazení rozdělovací funkce
    dist_plot = st.selectbox("Plot type", [px.box, px.histogram, px.violin])

    st.write(dist_plot(data, x=interesting_column, color=color))


if __name__ == "__main__":
    app()
