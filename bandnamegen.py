#!/usr/bin/python3
#!/bin/env/python3

"""Band name generator combines city name and pet name to produce unigue
band name."""
print("Welcome to the Band Name Generator.")
print("What's name of the city you grew up in?")
city = input()
print("What's your pet's name?")
pet_name = input()
band_name = city + " " + pet_name
print("Your band name could be {:s}".format(band_name))
