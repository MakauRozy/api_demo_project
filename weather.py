import requests

location =input("Enter your city: ")

url =f"https://api.weatherapi.com/v1/current.json?key=48eda227ccb146c2b8d100014262410&q={location}"
response= requests.get(url)

if response.status_code == 200:
    data= response.json()
    print(f"in {location} ,the temperature is {data["current"]["temp_c"]}degrees celcius, and the weather is {data["current"]["condition"]["text"]}")
else:
    print("something went wrong")


