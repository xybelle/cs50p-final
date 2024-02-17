import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    if valid_time[1] == "PM":
        h1, m1 = for_pm(valid_time[0])
    elif valid_time[1] == "AM":
        h1, m1 = for_am(valid_time[0])
    if valid_time[3] == "PM":
        h2, m2 = for_pm(valid_time[2])
    elif valid_time[3] == "AM":
        h2, m2 = for_am(valid_time[2])
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM) to ((?:1[0-2]|[1-9]):?[0-5]?[0-9]?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        sys.exit("Hours: time AM/PM to time AM/PM")


def for_pm(time):
    if ":" in time:
            h, m = time.split(":")
            h = int(h) + 12
            return h, int(m)
    else:
        h = int(time) + 12
        m = 0
        return h, m


def for_am(time):
    if ":" in time:
            h, m = time.split(":")
            return int(h), int(m)
    else:
        h = int(time)
        m = 0
        return h, m


if __name__ == "__main__":
    main()

