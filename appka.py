import re
import pandas as pd
import plotly.express as px
import streamlit as st


def app():
    st.title("Dashboard")
    # st.text("muzes sem zkusit neco nahrat, vytvorime")
    # vstup 1: výběr datové sady
    data_file_path = st.file_uploader("...to analyze your data")

    if data_file_path is None:
        st.warning("No data file uploaded yet")
        return

    # read data if user uploads a file
    data = pd.read_csv(data_file_path)
    relevant_columns = [column for column in data.columns if re.match(r'[Uu]nnamed|id|ID', column) is None]
    # seek back to position 0 after reading
    data_file_path.seek(0)

    # vstup 2: výběr parametrů scatter matrix
    dimensions = st.multiselect("Scatter matrix - choose relevant dimensions", list(data.columns), default=list(data.columns))
    color = st.selectbox("Color according to", relevant_columns)

    opacity = st.number_input('Opacity', max_value=1.0, min_value=0.0, value=0.5, step=0.1)
    # opacity = st.slider("Opacity", 0.0, 1.0, 0.5)

    # scatter matrix plot
    st.write(px.scatter_matrix(data, dimensions=dimensions, color=color, opacity=opacity))

    st.text("Plot interesting column")
    # výběr sloupce pro zobrazení rozdělení dat
    interesting_column = st.selectbox("Interesting column", relevant_columns)
    color_2 = st.selectbox("Color", relevant_columns, key='col2')
    # výběr funkce pro zobrazení rozdělovací funkce

    dist_plot = st.selectbox(
        "Plot type",
        [px.box, px.histogram, px.violin, px.strip, px.ecdf],
        index=1,
        format_func=lambda x: re.search(r'function(.*) at', str(x)).group(1)
    )

    st.write(dist_plot(data, x=interesting_column, color=color_2))


if __name__ == "__main__":
    app()
