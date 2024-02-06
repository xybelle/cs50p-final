def main():
    time = input("What time is it? ")
    t = convert(time)

    if t >= 7.0 and t <= 8.0:
        print("breakfast time")
    elif t >= 12.0 and t <= 13.0:
        print("lunch time")
    elif t >= 18.0 and t <= 19.0:
        print("dinner time")


def convert(time):
    h, m = map(float, time.split(':'))
    return h + m / 60


if __name__ == "__main__":
    main()
