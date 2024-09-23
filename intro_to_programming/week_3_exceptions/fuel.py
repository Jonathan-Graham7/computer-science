"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full,
1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains,
output E instead to indicate that the tank is essentially empty. And if 99% or more remains,
output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
ny exceptions like ValueError or ZeroDivisionError.
"""
def main():
    fuel_percent = fuelInput()
    if fuel_percent <= 1:
        print("E")
    elif fuel_percent >= 99:
        print("F")
    else:
        print(f"{fuel_percent}%")

def fuelInput():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
        except ValueError:
            continue
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            continue
        try:
            fraction = x / y
        except ZeroDivisionError:
            continue
        if x > y:
            continue
        else:
            break
    return round(fraction * 100)

main()