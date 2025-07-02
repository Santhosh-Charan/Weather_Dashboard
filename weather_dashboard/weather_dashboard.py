import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

API_KEY = "YOUR_API_KEYS"

@st.cache_data
def fetch_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    return requests.get(url, params=params).json()

def main():
    st.title("Live Weather Dashboard")
    city = st.text_input("Enter city:", "Hyderabad")
    if st.button("Fetch Weather"):
        data = fetch_weather(city)
        if data.get("cod") == 200:
            df = pd.json_normalize(data)
            st.metric("Temperature (°C)", df["main.temp"][0])
            st.metric("Humidity (%)", df["main.humidity"][0])
            fig, ax = plt.subplots()
            ax.bar(["Temp", "Humidity"],
                   [df["main.temp"][0], df["main.humidity"][0]],
                   color=["red", "blue"])
            st.pyplot(fig)
        else:
            st.error(f"Error: {data.get('message', 'Unknown')}")
            
if __name__ == "__main__":
    main()
