import streamlit as st
import pandas as pd
import numpy as np


def get_info():
    df = st.session_state.df
    df = pd.DataFrame(df)
    d = {}
    for col in df.columns:
        if np.issubdtype(df[col].dtype, np.number):
            d[col]={
                'Count':df[col].count(),
                'Datatype': df[col].dtype,
                'NA': df[col].isna().sum(),
                'Unique': df[col].nunique(),
                'Mean': df[col].mean(),
                'Std': df[col].std(),
            }
        else:
            d[col] = {
                'Count': df[col].count(),
                'Datatype': df[col].dtype,
                'NA': df[col].isna().sum(),
                'Unique': df[col].nunique(),
                'Mean': np.nan,
                'Std': np.nan,
            }
    info_df = pd.DataFrame(d)
    st.dataframe(info_df)

