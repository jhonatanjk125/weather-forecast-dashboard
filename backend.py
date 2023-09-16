import requests

def get_data(place, forecast_days):
    API_KEY = "22fc83554e8e785d568edd5a38852034"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    raw_data = response.json()
    raw_data = raw_data['list'][0:forecast_days * 8]
    return raw_data

if __name__=="__main__":
    data=get_data("Bogota", 3)
    print(data)
    print(data.keys())
