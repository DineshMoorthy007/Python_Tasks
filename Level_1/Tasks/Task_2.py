def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

try:
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()

    if unit == 'C':
        converted = celsius_to_fahrenheit(value)
        print(f"{value}°C is equal to {converted:.2f}°F")
    elif unit == 'F':
        converted = fahrenheit_to_celsius(value)
        print(f"{value}°F is equal to {converted:.2f}°C")
    else:
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

except ValueError:
    print("Invalid temperature input. Please enter a numeric value.")