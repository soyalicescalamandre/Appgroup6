import json

import requests  # pip install requests
import streamlit as st  # pip install streamlit
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

st.set_page_config(
    page_title = "Multipage App",
    page_icon='📊',
)

st.title ("Homepage")
st.sidebar.success("Select a page above.")
st.header('Welcome to this amazing app built by my three best friends!')



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_3vbOcw.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    #renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)

st.caption('If you do not know them, their names are: Alice, Sara and Laura.')
st.subheader('What is this app for?')
st.caption('This app can be used to check electricity prices of Spain in the previous days. \
            If you look on the sidebar, there are two possibilities.')
st.subheader('Buttons')
st.caption('There are going to be three persuasive buttons between the ones you have to chose.\
            Each of them will give you info regarding a prices for a specific amount of time in the past.')
st.subheader('Slider')
st.caption('This page is even better! You can deliberatly choose the amount of time you want to go back in time!')
st.header('Have fun! 🙌')

