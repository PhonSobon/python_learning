#Write a program to convert a temperature from Celsius to Fahrenheit using this formula:
# Fahrenheit = (Celsius * 9/5) + 32
# Celsius to Fahrenheit Converter
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")