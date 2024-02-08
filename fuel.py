def main():
    percent = get_fraction()

    if percent <= 0.01:
        print("E")
    elif percent >= 99:
        print("F")
    else:
        print(f"{int(percent)}%")


def get_fraction():
    while True:
        try:
            fraction = input("Fraction: ").split('/')
            percent = (int(fraction[0]) / int(fraction[1])) * 100
            if percent > 100:
                raise ExceedHundred
            return percent
        except (ValueError, ZeroDivisionError, ExceedHundred):
            pass


class ExceedHundred(Exception):
    pass


main()
