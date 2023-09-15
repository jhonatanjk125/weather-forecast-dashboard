import streamlit as st
import plotly.express as px

st.title("Weather forecast")
city = st.text_input("Please enter the city:")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Number of days to forecast")
option = st.selectbox("Select the type of data to display", ("Temperature", "Sky conditions"))
st.subheader(f"{option} for the next {days} days in {city}")


dates = ["2023-12-09","2023-12-10","2023-12-11"]
temperatures = [12, 14, 21]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
st.plotly_chart(figure)