import tkinter as tk
import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather():
    location = ""
    if location_var.get() == "city":
        location = city_entry.get().strip()
    elif location_var.get() == "zip":
        location = zip_entry.get().strip()
    if location:
        weather_data = get_weather(api_key, location)
        if weather_data["cod"] == 200:
            location_label.config(text=weather_data["name"])
            temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
            humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
            conditions_label.config(text=f"Weather Conditions: {weather_data['weather'][0]['description']}")
        else:
            location_label.config(text="Error")
            temperature_label.config(text="")
            humidity_label.config(text="")
            conditions_label.config(text=weather_data["message"])
    else:
        location_label.config(text="Please enter a city name or ZIP code")
        temperature_label.config(text="")
        humidity_label.config(text="")
        conditions_label.config(text="")

def clear_entry():
    city_entry.delete(0, tk.END)
    zip_entry.delete(0, tk.END)

def toggle_entry():
    if location_var.get() == "city":
        city_entry.config(state="normal")
        zip_entry.config(state="disabled")
    elif location_var.get() == "zip":
        city_entry.config(state="disabled")
        zip_entry.config(state="normal")
    clear_entry()

root = tk.Tk()
root.title("Weather App")

api_key = "8d543bc0c5964b377a72a905ea9486d5"  

location_label = tk.Label(root, text="")
location_label.grid(row=0, column=0, padx=10, pady=5, columnspan=2)

location_frame = tk.Frame(root)
location_frame.grid(row=1, column=0, padx=10, pady=5, columnspan=2)

location_var = tk.StringVar()
location_var.set("city")
city_radio = tk.Radiobutton(location_frame, text="City", variable=location_var, value="city", command=toggle_entry)
city_radio.grid(row=0, column=0, padx=5, pady=5)
city_radio.select()

zip_radio = tk.Radiobutton(location_frame, text="ZIP Code", variable=location_var, value="zip", command=toggle_entry)
zip_radio.grid(row=0, column=1, padx=5, pady=5)

city_entry = tk.Entry(root)
city_entry.grid(row=2, column=0, padx=10, pady=5)

zip_entry = tk.Entry(root)
zip_entry.grid(row=2, column=1, padx=10, pady=5)
zip_entry.config(state="disabled")

search_button = tk.Button(root, text="Search", command=display_weather)
search_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

temperature_label = tk.Label(root, text="")
temperature_label.grid(row=4, column=0, padx=10, pady=5, columnspan=2)

humidity_label = tk.Label(root, text="")
humidity_label.grid(row=5, column=0, padx=10, pady=5, columnspan=2)

conditions_label = tk.Label(root, text="")
conditions_label.grid(row=6, column=0, padx=10, pady=5, columnspan=2)

root.mainloop()
