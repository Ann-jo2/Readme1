import streamlit as st
import pandas as pd
df = pd.read_csv('vehicles_us (2).csv')
st.write(df.head())