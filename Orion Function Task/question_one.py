def temperature_converter(temperature, measurement):
    if measurement.upper() == "F":
        calc = (temperature - 32) * 5/9 # to celcius
        if calc > 28:
            return "Heat alert"
    else:
        calc = (temperature - 9/5) + 32 # to fahrenheit
        if calc < 82:
            return "Cold advisory"
            
   
temperature = float(input("Enter temperature(value): "))
temperature_unit = input("Enter unit of measurement: C or F: ")


print(temperature_converter(temperature, temperature_unit))
