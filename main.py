import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast")
city = st.text_input("Please enter the city:")
days = st.slider("Forecast days", min_value=1, max_value=5, help="Number of days to forecast")
option = st.selectbox("Select the type of data to display", ("Temperature", "Sky conditions"))
st.subheader(f"{option} for the next {days} days in {city}")

try:
    # Plot either temperature or sky conditions based on user selection
    if city:
        # Get the temperature, sky data
        raw_data=get_data(city, days)
        if option == "Temperature":
            data = {raw_data[index]['dt_txt'] : raw_data[index]['main']['temp']-273.15 for index in range(len(raw_data))}
            # Create temperature plot
            figure = px.line(x=data.keys(), y=data.values(), labels={"x": "Date", "y": "Temperature (C)"})
            st.plotly_chart(figure)
        if option == "Sky conditions":
            data = {raw_data[index]['dt_txt']: raw_data[index]['weather'][0]['main'] for index in range(len(raw_data))}
            print(data.values())
            conditions_list = data.values()
            image_paths = [f"images/{list(conditions_list)[i].lower()}.png" for i in range(len(conditions_list))]
            st.image(image_paths, width=140)
except KeyError:
    st.write('<strong><p style="color:red">The city you entered is invalid, '
             'please check your input and try again</p></strong>', unsafe_allow_html=True)