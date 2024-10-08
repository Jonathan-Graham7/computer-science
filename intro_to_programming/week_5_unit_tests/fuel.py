def main():
    while True:
        fraction = input("Fraction: ")
        try:
            fuel_amount = convert(fraction)
        except (ValueError, ZeroDivisionError):
            continue
        else:
            break
    status = gauge(fuel_amount)
    print(status)

def convert(fraction):
    x, y = fraction.split("/")
    if x.isdigit() and y.isdigit():
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            return round(x / y * 100)
    else:
        raise ValueError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
