import requests

def Gen_report(c):
    url = f"https://wttr.in/Chennai,India"
    try:
        data = requests.get(url, timeout=10, headers={"User-Agent": "curl"})
        print(data.text)
    except requests.exceptions.RequestException:
        print("Error occurred while fetching weather")

city_name = input("Enter city or country: ")
Gen_report(city_name)
