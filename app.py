import streamlit as st
# Set the app in wide view
st.set_page_config(layout="wide") 
import time

# Loading data from different scripts
from load import stock_list, intervals, chart_data
from chart import display_chart, charts

st.sidebar.image("logo.jpg", use_container_width=True, width=5000)

# Sidebar 
st.sidebar.title('Choose an Option')
stock = st.sidebar.selectbox(
    'Select stock:',
    stock_list
)

interval = st.sidebar.selectbox(
    'Select interval:',
    intervals
)

chart = st.sidebar.selectbox(
    'Select chart:',
    charts
)

nofs = [{'Pattern': 'Bearish Engulfing', 'Time': '2021-09-01 09:00:00', 'Stock': 'HINDALCO', 'Interval': '1d'},
        {'Pattern': 'Bearish Engulfing', 'Time': '2021-09-01 09:00:00', 'Stock': 'HINDALCO', 'Interval': '1d'}]
# Notifications Sidebar
st.sidebar.title('Notifications')
st.sidebar.markdown(f"""
<div style=" overflow-y: auto; background-color: #0E1118; padding: 10px; border-radius: 8px;">
    {"".join([f"<p><strong>{notification['Pattern']}</strong> at {notification['Time']} for {notification['Stock']} ({notification['Interval']})</p>" for notification in nofs])}
</div>
""", unsafe_allow_html=True)

with st.empty():
    data = chart_data(chart, stock, interval)
    date = True
    if interval == '1d':
        date = False
    display_chart(chart, data, key=f"{chart}_{time.time()}", date=date)
    time.sleep(60)