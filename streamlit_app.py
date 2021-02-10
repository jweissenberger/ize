import streamlit as st
import pandas as pd
import time


df = pd.DataFrame(
    [
        {'building': 'Empire State', 'location': "NYC", 'height':1000},
        {'building': 'B', 'location': "LA", 'height':600},
        {'building': 'c', 'location': "Paris", 'height':900},
        {'building': 'C', 'location': "SF", 'height':800},
        {'building': 'P', 'location': "Dallas", 'height':500},
    ]
)



st.title('IZE')
st.subheader('Use natural language to visualize and analyze your data')

st.dataframe(df.head())

example = 'Ex: How many rows are there?'
user_input = st.text_input("Input your Query here", example)

if user_input and user_input != example:
    with st.spinner("Loading..."):
        time.sleep(2)

        if user_input:
            st.text(user_input)


