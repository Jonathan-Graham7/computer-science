def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() and not s[1].isalpha():
        return False
    previous_char = ""
    for char in s:
        if previous_char.isalpha():
            if char == "0":
                return False
        if previous_char.isnumeric():
            if char.isalpha():
                return False
        previous_char = char
    return True

if __name__ == "__main__":
    main()