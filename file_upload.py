import streamlit as st
import pandas as pd

def get_upload_file_ui():
    st.title("📊 AutoViz - One Click Data Visualization")
    st.write("Welcome to AutoViz! Upload your file and generate graphs instantly.")
    uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])
    if st.session_state.uploaded_file:
        st.success(f"File {st.session_state.uploaded_file.name} uploaded successfully!")
        st.dataframe(st.session_state.df)
    if uploaded_file:
        st.session_state.uploaded_file = uploaded_file
        df = pd.read_csv(st.session_state.uploaded_file)
        df.columns = df.columns.str.capitalize()
        st.session_state.df=df
        st.success("File uploaded successfully!")
        st.dataframe(st.session_state.df)

