def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s[0:2].isalpha():
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    first_number = False
    for c in s:
        if not c.isalnum():
            return False
        if c.isdigit() and first_number == False:
            first_number = True
            if c == '0':
                return False
        if c.isalpha() and first_number == True:
            return False

    return True


main()
