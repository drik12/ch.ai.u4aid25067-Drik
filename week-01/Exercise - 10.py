temperature_c = float(input("Enter the temperature in Celsius: "))
temperature_f = (temperature_c * 9/5) + 32
print("Temperature in Fahrenheit:", temperature_f)

if temperature_c < 0:
    print("Very cold! Wear thick jacket")
elif 0 <= temperature_c <= 15:
    print("Cold. Wear jacket")
elif 16 <= temperature_c <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")