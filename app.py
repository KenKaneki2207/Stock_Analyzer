import streamlit as st
st.set_page_config(layout="wide")

import streamlit.components.v1 as components
from load import *
from pattern import *
from tp import *

# Sidebar for stock selection
st.sidebar.title('Choose an Option')
stock = st.sidebar.selectbox(
    'Select stock:',
    stock_list
)

# Sidebar for intervals 
interval = st.sidebar.selectbox(
    'Select interval:',
    intervals
)

# Sidebar for chart selection
chart = st.sidebar.selectbox(
    'Select chart:',
    charts
)

col1, col2 = st.columns([3, 1])

# Embed the HTML content in the first column
with col1:
    if chart == 'Candle':
        df = pd.read_csv(f'stock_data/{interval}/{stock}.csv')
        data = df.to_dict(orient='records')

        # Plot the candlestick pattern with the interval
        candle_stick(data)

    if chart == "Line":
        df = pd.read_csv(f'stock_data/{interval}/{stock}.csv')
        df = df[['time', 'close']]
        df = df.rename(columns={'close':'value'})
        data = df.to_dict(orient='records')

        line_chart(data)

with col2:
    # Read the HTML content from right_sidebar.html
    with open('notification.html', 'r') as file:
        right_sidebar_html = file.read()
    components.html(right_sidebar_html)