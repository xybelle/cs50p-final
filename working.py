import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid_time = validate_input(s)
    #print(valid_time)
    #print(valid_time[0])
    if re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[0]):
        h, m1 = valid_time[0].split(":")
        h1 = hours_mins_fmt(h, valid_time[1])
    elif re.search(r"(?:1[0-2]|[1-9])", valid_time[0]):
        h1 = hours_fmt(valid_time[0], valid_time[1])
        m1 = 0
    if re.search(r"(?:1[0-2]|[1-9]):[0-5][0-9]", valid_time[2]):
        hh, m2 = valid_time[2].split(":")
        h2 = hours_mins_fmt(hh, valid_time[3])
    elif re.search(r"(?:1[0-2]|[1-9])", valid_time[2]):
        h2 = hours_fmt(valid_time[2], valid_time[3])
        m2 = 0
    #print(f"{h1:02}:{m1:02} to {h2:02}:{m2:02}")
    return f"{h1:02}:{m1:02} to {h2:02}:{m2:02}"


def validate_input(s):
    try:
        if matches := re.search(r"((?:1[0-2]|[1-9]):?(?:[0-5][0-9])?) (AM|PM) to ((?:1[0-2]|[1-9]):?(?:[0-5][0-9])?) (AM|PM)", s):
            return matches.groups()
        else:
            raise ValueError
    except ValueError:
        print("Hour: time AM/PM to time AM/PM")


def hours_mins_fmt(hour, mid):
    if mid == "AM":
        if  hour == "12":
            hour = 0
        return int(hour)
    if mid == "PM":
        if hour != "12":
            hour = int(hour) + 12
        return int(hour)


def hours_fmt(hour, mid):
    if mid == "AM":
        if hour == "12":
            hour = 0
        return int(hour)
    if mid == "PM":
        if hour != "12":
            hour = int(hour) + 12
        return int(hour)


if __name__ == "__main__":
    main()
