import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_pie_chart():
    df = st.session_state.df
    df = pd.DataFrame(df)
    columns = []
    for col in df.columns:
        if df[col].nunique()<=10:
            columns.append(col)
    options = columns
    selected_option = st.selectbox("Select an option:", options)
    plt.style.use("dark_background")
    colors = sns.color_palette("dark", len(df[selected_option].value_counts().index))
    fig, ax = plt.subplots()
    ax.pie(df[selected_option].value_counts(), labels=df[selected_option].value_counts().index,
           autopct='%1.1f%%', startangle=90,wedgeprops={'edgecolor': 'black'},colors=colors)
    plt.xticks(rotation=90)
    st.pyplot(fig)