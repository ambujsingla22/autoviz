import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_scatter_plot():
    df = st.session_state.df
    df = pd.DataFrame(df)
    columns = []
    for col in df.columns:
        if df[col].nunique() <= 100:
            columns.append(col)
    options = columns
    selected_option_1 = st.selectbox("Select 1st column:", options)
    selected_option_2 = st.selectbox("Select 2nd column:", options)
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=selected_option_1, y=selected_option_2)
    plt.xticks(rotation=90)
    st.pyplot(fig)