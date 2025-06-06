FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    temperature=(fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"temperature converted to Celsius: {temperature}")
    return temperature

def convert_to_fahrenheit(celsius):
    temperature_converted_Fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR +32
    print(f" temperature converted to Fahrenheit: { temperature_converted_Fahrenheit}")
    return  temperature_converted_Fahrenheit

temp = float(input("Enter the temperature to convert: "))
specific_temp=input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

match specific_temp:
    case 'C':
        print(f"{temp} is {convert_to_fahrenheit}")
    case 'F':
        print(f"{temp} is {convert_to_celsius}")
    case _ :
        print('Invalid temperature. Please enter a numeric value.')

