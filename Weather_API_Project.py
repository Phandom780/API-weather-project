import tkinter as tk
import requests

API_KEY = "YOUR_API_KEY"


def get_weather():
    city = city_entry.get()

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        condition = data["weather"][0]["description"]

        result_label.config(
            text=f"{city}\nTemperature: {temperature}°F\nCondition: {condition.title()}"
        )
    else:
        result_label.config(text="City not found. Try again.")


# Create window
window = tk.Tk()
window.title("Weather App")
window.geometry("350x300")

# Title
title_label = tk.Label(window, text="Weather App", font=("Arial", 22))
title_label.pack(pady=20)

# City input
city_entry = tk.Entry(window, font=("Arial", 14))
city_entry.pack(pady=10)

city_entry.insert(0, "Enter city")

# Button
weather_button = tk.Button(
    window,
    text="Get Weather",
    command=get_weather,
    font=("Arial", 12)
)
weather_button.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 14)
)
result_label.pack(pady=20)

# Run app
window.mainloop()
