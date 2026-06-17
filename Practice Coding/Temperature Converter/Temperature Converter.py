def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp = float(input("Enter Temperature: "))

result = celsius_to_fahrenheit(temp)

print("Temperature in Fahrenheit:", result, "°F")
