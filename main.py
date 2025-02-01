import streamlit as st 
import requests 
import pandas as pd
import numpy as np
import datetime 

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

local_css("styles.css")


st.title("Weather :blue[Dashboard]")

Colombo_resp = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=6.9355&longitude=79.8487&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,surface_pressure,wind_speed_10m&hourly=temperature_2m&daily=apparent_temperature_max,apparent_temperature_min,precipitation_sum,wind_speed_10m_max")
Jaffna_resp = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=9.6684&longitude=80.0074&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,surface_pressure,wind_speed_10m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max")
Nuwara_Eliya_resp = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=6.9708&longitude=80.7829&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,surface_pressure,wind_speed_10m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max")
Anuradhapura_resp = requests.get ("https://api.open-meteo.com/v1/forecast?latitude=8.3122&longitude=80.4131&current=temperature_2m,relative_humidity_2m,is_day,precipitation,rain,surface_pressure,wind_speed_10m&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max")

value_C = Colombo_resp.json()

value_J = Jaffna_resp.json()

value_N = Nuwara_Eliya_resp.json()

value_A = Anuradhapura_resp.json()

options = ["Temperature", "Humidity","Rainfall","Wind speed", "Pressure"]
selection = st.pills("Weather elements", options, selection_mode="single" )
st.markdown(f"You've selected: {selection}.")

if selection == "Temperature":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Colombo", value_C['current']['temperature_2m'], "1.2 °C")
    col2.metric("Jaffna", value_J['current']['temperature_2m'], "1.0 °C")
    col3.metric("Anuradhapura", value_A['current']['temperature_2m'], "1.2 °C")
    col4.metric("Nuwara Eliya", value_N['current']['temperature_2m'], "-1.0 °C")

elif selection == "Humidity":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Colombo", value_C['current']['relative_humidity_2m'], "1%")
    col2.metric("Jaffna", value_J['current']['relative_humidity_2m'], "-1%")
    col3.metric("Anuradhapura", value_A['current']['relative_humidity_2m'], "1.5%")
    col4.metric("Nuwara Eliya", value_N['current']['relative_humidity_2m'], "2%")

elif selection == "Rainfall":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Colombo", value_C['current']['rain'], "-0%")
    col2.metric("Jaffna",value_J['current']['rain'], "-0%")
    col3.metric("Anuradhapura", value_A['current']['rain'], "-0%")
    col4.metric("Nuwara Eliya", value_N['current']['rain'], "-0%")

elif selection == "Wind speed":
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Colombo", value_C['current']['wind_speed_10m'], "1km/h")
    col2.metric("Jaffna", value_J['current']['wind_speed_10m'], "-1km/h")
    col3.metric("Anuradhapura", value_A['current']['wind_speed_10m'], "-2km/h")
    col4.metric("Nuwara Eliya", value_N['current']['wind_speed_10m'], "2km/h")


else:
     col1, col2, col3, col4 = st.columns(4)
     col1.metric("Colombo" ,value_C['current']['surface_pressure'] , "-1 hPa")
     col2.metric("Jaffna" , value_J['current']['surface_pressure'], "1 hPa")
     col3.metric("Anuradhapura" , value_A['current']['surface_pressure'], "-2 hPa")
     col4.metric("Nuwara Eliya" , value_N['current']['surface_pressure'], "1 hPa")



date_pick = st.sidebar.date_input("Choose specific date - Within next 7 days", value=None)
st.sidebar.write("Date:", date_pick)


option_side= ["Temperature","Percipitation"]
selection_side = st.sidebar.pills("Weather predictions", option_side, selection_mode="single" )
st.sidebar.markdown(f"You've selected: {selection_side}.")

col5, col6 = st.sidebar.columns(2)

# if date_pick in value_C ["daily"] ["time"]:
#      if selection_side == "Temperature":
#         col5.metric ("Mix (°C)", value_C ["daily"] ["apparent_temperature_max"])
#         col6.metric ("Min (°C)", value_C ["daily"] ["apparent_temperature_min"])
#      else:
#          col5.metric (value_C ["daily"] ["precipitation_sum"])
#          col6.metric ()
# else: 
#     st.sidebar.write ("Nothin")

chart_data = pd.DataFrame({
    "Colombo": value_C["daily"]["precipitation_sum"],
    "Nuwara Eliya": value_N["daily"]["precipitation_sum"]
})

st.area_chart(chart_data)

if value_C ['current']['is_day'] == 1:
    st.image("hanoi-1528199_1280.jpg", caption="City")

else: 
   st.image("sunset-7154934_1280.jpg", caption="City")