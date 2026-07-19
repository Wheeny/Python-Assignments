temperature_in_celcius = input("Enter temperature in Celcius: ")
temperature_in_farenheit  = int(temperature_in_celcius) * (9/5) + 32
temperature_in_kelvin  = float(temperature_in_celcius) + 273.15

print("Temperature in Farenheit is : ", temperature_in_farenheit)
print("Temperature in Kelvin is : ", temperature_in_kelvin)