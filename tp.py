import streamlit as st

# Inject custom CSS to create a right-side sidebar
st.markdown("""
    <style>
        .css-1d391kg {
            display: flex;
            flex-direction: row-reverse;
        }
        .css-1d391kg .stSidebar {
            order: -1;
        }
        .css-1d391kg .stContent {
            margin-right: 320px;  /* Adjust this value based on the sidebar width */
        }
    </style>
""", unsafe_allow_html=True)

