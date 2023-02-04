#!/usr/bin/env python3
"""Convert dictionary of temperature in celcius to fahrenheit"""

weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
}

weather_f = {day:round((celcius * 1.8) + 32, 2) for day, celcius in weather_c.items()}
print(weather_f)
