import requests
from tkinter import Tk, Label, Entry, Button, Text, END


def fetch_weather():
    api_key = "96cd03e854c0838ca4c828057ce2a1a3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = city_entry.get() 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    
    response = requests.get(complete_url)
    x = response.json()
    
    output_box.delete("1.0", END)
    
    if x["cod"] != "404":
        if "main" in x:
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            result = (f"City: {city_name}\n"
                      f"Temperature (K): {current_temperature}\n"
                      f"Pressure (hPa): {current_pressure}\n"
                      f"Humidity (%): {current_humidity}\n"
                      f"Description: {weather_description}")
        else:
            result = "Weather data is not available for the specified city."
    else:
        result = "City Not Found"
    
    output_box.insert(END, result)


def refresh_app():
    """Clear the input and output fields."""
    city_entry.delete(0, END)  # Clear the city name entry field
    output_box.delete("1.0", END)  # Clear the output box


# Create the GUI window
app = Tk()
app.title("Weather App")
app.geometry("400x350")

# Add GUI elements
Label(app, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = Entry(app, font=("Arial", 12), width=30)
city_entry.pack(pady=5)

Button(app, text="Get Weather", font=("Arial", 12), command=fetch_weather).pack(pady=10)

output_box = Text(app, font=("Arial", 12), width=40, height=10, wrap="word")
output_box.pack(pady=10)

# Add the Refresh button
Button(app, text="Refresh", font=("Arial", 12), command=refresh_app).pack(pady=5)

# Run the GUI
app.mainloop()
