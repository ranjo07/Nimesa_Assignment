import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"


def get_weather_data():
    response = requests.get(API_URL)
    return response.json()


def get_temperature(date):
    weather_data = get_weather_data()
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["temp"]
    return None


def get_wind_speed(date):
    weather_data = get_weather_data()
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["wind"]["speed"]
    return None


def get_pressure(date):
    weather_data = get_weather_data()
    for forecast in weather_data["list"]:
        if date in forecast["dt_txt"]:
            return forecast["main"]["pressure"]
    return None


def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            temperature = get_temperature(date)
            if temperature is not None:
                print(f"Temperature at {date}: {temperature} Kelvin")
            else:
                print("Weather data not found for the given date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed at {date}: {wind_speed} m/s")
            else:
                print("Weather data not found for the given date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:mm:ss): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure at {date}: {pressure} hPa")
            else:
                print("Weather data not found for the given date.")
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
