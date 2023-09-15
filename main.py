import streamlit as st

st.title("Weather forecast")
city = st.text_input("Please enter the city:")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Number of days to forecast")
option = st.selectbox("Select the type of data to display", ("Temperature", "Sky conditions"))
st.subheader(f"{option} for the next {days} days in {city}")