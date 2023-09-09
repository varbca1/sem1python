def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit - 32) * 5/9

celsius = int(input("celsius: "))
fahrenheit = int(input("fahrenheit: "))

print("Temprature in celsius is: ", celsius_to_fahrenheit(celsius))

print(celsius_to_fahrenheit("Temprature in fahrenheit is: ",fahrenheit))