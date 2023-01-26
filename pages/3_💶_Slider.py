import streamlit as st
# import requests library
import requests 
import csv
import json
import pandas as pd
from datetime import date, datetime, timedelta #we need it to ask files to the API
import numpy as np

if "days" not in st.session_state:
    # set the initial default value of the slider widget
    st.session_state.days = -1.00

st.title('Electricity prices')
st.caption('In this page you have more freedom. Enojy it!')
st.header('How does it work?')
st.caption('Moving the slider, it is possible to decide how much data the REE API has to retrive.')
st.caption('The limits of the slider are -3 (three days ago) and -0.1. Due to the fact that the value 0 would not produce any results.')
st.caption('As mentioned above, here there is more freedom. Feel free to choose how many days, or portions of it, you want to consider.')


st.slider(
    "Time to make a choice ☺️",
    min_value=-3.00,
    max_value=-0.1,
    key="days"
)

# This will get the value of the slider widget
st.write(st.session_state.days)

end_date = datetime.now() #+ timedelta(hours=1)
start_date = end_date + timedelta(days=st.session_state.days)             # ERROR if we try to take info for a whole year
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

st.line_chart(data = yesterday)#, x="Number of hours", y="Electricity prices [MW/h]")

st.caption('The prices are in €/MWh.')
