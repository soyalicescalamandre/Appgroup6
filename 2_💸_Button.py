#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 19:24:45 2023

@author: Alice
"""

import streamlit as st
# import requests library
import requests 
import csv
import json
import pandas as pd
# import plotting library
import matplotlib
import matplotlib.pyplot as plt 
from datetime import date, datetime, timedelta #we need it to ask files to the API
import numpy as np


# Configuration of the page
st.set_page_config(
    page_title='Electricity Prices',
    page_icon='📊')


st.title('Electricity prices')
st.caption('In this page you need to choose a button. Each of them is more persuasive, tough choise! ')


#YESTERDAY

end_date = datetime.now() #+ timedelta(hours=1)
start_date = end_date - timedelta(days=1)             # ERROR if we try to take info for a whole year
# transform into strings with a minute resolution
end_date = end_date.strftime('%Y-%m-%dT%H:%M')
start_date = start_date.strftime('%Y-%m-%dT%H:%M')

endpoint = 'https://apidatos.ree.es' #
get_archives = '/en/datos/mercados/precios-mercados-tiempo-real' #directory in the server - real time market price - you can get this reading the API documentation
headers = {'Accept': 'application/json',
           'Content-Type': 'application/json',
           'Host': 'apidatos.ree.es'} #this is written in the documentation 
params_1 = {'start_date': start_date, 'end_date': end_date, 'time_trunc':'hour'}
response_1 = requests.get(endpoint+get_archives, headers=headers, params=params_1)
data_json_1 = response_1.json()

#the followings are the data forecasted
pvpc_price_values_1 = data_json_1['included'][0]['attributes']['values']
pvpc_price_1da = []

for time_period in pvpc_price_values_1:
    #print(time_period['value'])
    pvpc_price_1da.append(time_period['value'])


yesterday = pd.DataFrame(
    pvpc_price_1da,
    columns=['Prices'])

#TWO DAYS AGO

end_date_2 = datetime.now() #+ timedelta(hours=1)
start_date_2 = end_date_2 - timedelta(days=2)             # ERROR if we try to take info for a whole year
# transform into strings with a minute resolution
end_date_2 = end_date_2.strftime('%Y-%m-%dT%H:%M')
start_date_2 = start_date_2.strftime('%Y-%m-%dT%H:%M')
params_2 = {'start_date': start_date_2, 'end_date': end_date_2, 'time_trunc':'hour'}
response_2 = requests.get(endpoint+get_archives, headers=headers, params=params_2)
data_json_2 = response_2.json()

#the followings are the data forecasted
pvpc_price_values_2 = data_json_2['included'][0]['attributes']['values']
pvpc_price_2da = []

for time_period in pvpc_price_values_2:
    #print(time_period['value'])
    pvpc_price_2da.append(time_period['value'])


twodaysago = pd.DataFrame(
    pvpc_price_2da,
    columns=['Prices'])

#THREE DAYS AGO

end_date_3 = datetime.now() #+ timedelta(hours=1)
start_date_3 = end_date_3 - timedelta(days=3)             # ERROR if we try to take info for a whole year
# transform into strings with a minute resolution
end_date_3 = end_date_3.strftime('%Y-%m-%dT%H:%M')
start_date_3 = start_date_3.strftime('%Y-%m-%dT%H:%M')
params_3 = {'start_date': start_date_3, 'end_date': end_date_3, 'time_trunc':'hour'}
response_3 = requests.get(endpoint+get_archives, headers=headers, params=params_3)
data_json_3 = response_3.json()

#the followings are the data forecasted
pvpc_price_values_3 = data_json_3['included'][0]['attributes']['values']
pvpc_price_3da = []

for time_period in pvpc_price_values_3:
    #print(time_period['value'])
    pvpc_price_3da.append(time_period['value'])


threedaysago = pd.DataFrame(
    pvpc_price_3da,
    columns=['Prices'])


if st.button('For yesterday'):
    st.line_chart(yesterday)
    st.write('There you have it! The prices are in €/MWh.')
else:
    st.write('Choose me 🤩')
    
if st.button('For the last two days'):
    st.line_chart(twodaysago)
    st.write('There you have it! The prices are in €/MWh.')
else:
    st.write('Choose meeeee 🥹')

if st.button('For the last three days'):
    st.line_chart(threedaysago)
    st.write('There you have it! The prices are in €/MWh.')
else:
    st.write('Choose me!!!!! 🙏')
    
