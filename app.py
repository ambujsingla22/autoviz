import streamlit as st
from streamlit_option_menu import option_menu
from file_upload import get_upload_file_ui
from view_data import  get_info
from view_bar_graph import get_bar_graph
from view_pie_chart import get_pie_chart
from view_scatter_plot import get_scatter_plot


if 'uploaded_file' not in st.session_state:
    st.session_state.uploaded_file = None
if 'df' not in st.session_state:
    st.session_state.df = None  # Initial shared data

with st.sidebar:
    selected = option_menu(
        menu_title="AutoViz",
        options=["Upload File", "Info", "Bar Graphs", "Pie Charts",
                 "Relationships Graphs"],
        icons=["upload", "info", "bar-chart", "pie-chart",
               "rulers"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Upload File":
    get_upload_file_ui()


if selected == "Info":
    get_info()

if selected == "Bar Graphs":
    get_bar_graph()

if selected == "Pie Charts":
    get_pie_chart()

if selected == "Relationships Graphs":
    get_scatter_plot()