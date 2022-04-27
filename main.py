import requests
import smtplib

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
MY_KEY = "7faee3fad0683058979c912ce7f55a8a"
EMAIL = "edernonato47teste@hotmail.com"
PASSWORD = "Eder@teste321"

parameters = {
    "appid": MY_KEY,
    "lat": -23.550520,
    "lon": -46.633308,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()


twelve_hour_forecast = weather_data["hourly"][:12]
should_bring = False
id_weather_list = [weather_data["hourly"][value]["weather"][0]["id"] for value in range(len(twelve_hour_forecast))]

for item in id_weather_list:
    if item < 700:
        should_bring = True

if should_bring:
    connection = smtplib.SMTP("smtp-mail.outlook.com", 587)
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(from_addr=EMAIL, to_addrs="edernonato47teste@hotmail.com", msg="Subject: It will rain!\n\n Today will"
                                                                                  " rain, you should bring an umbrella!")

