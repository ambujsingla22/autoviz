import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_bar_graph():
    df = st.session_state.df
    df = pd.DataFrame(df)
    columns = []
    for col in df.columns:
        if df[col].nunique()<=100:
            columns.append(col)
    options = columns
    selected_option = st.selectbox("Select an option:", options)
    plt.style.use("dark_background")
    fig, ax = plt.subplots()
    sns.countplot(data=df,x=selected_option,palette="dark",linewidth=1,
                  edgecolor="white",)
    for p in ax.patches:
        ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom',
                    fontsize=8, color='white')

    plt.xticks(rotation=90)
    st.pyplot(fig)