import streamlit as st
import pandas as pd
import numpy as np

DATA_URL = '~/working/datasets/house_prices/Seattle_house_listings.csv'

@st.cache_data
def load_data(file):
    data = pd.read_csv(DATA_URL)
    return data

st.title('Seattle house prices')

# data_load_state = st.text('Loading data...')
data = load_data(DATA_URL)
# data_load_state.text("Done!")

if st.checkbox('Show raw data'):
    st.write(data)

neighborhoods = data['neighborhood'].drop_duplicates()

neigh_choice = st.selectbox('Neighborhood:',neighborhoods)

st.bar_chart(data.loc[(data['neighborhood']==neigh_choice)], x="neighborhood", y="listed_price", color="n_bedrooms", stack=False)