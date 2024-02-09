months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
    while True:
        try:
            date = input("Date: ")
            if '/' in date:
                date = date.split('/')
            if ' ' in date:
                date = date.split()
            m = check_month(date[0])
            d = check_day(date[1].rstrip(','))
            y = check_year(date[2])
            print(f"{y}-{m:02}-{d:02}")
            break
        except (KeyError, ValueError):
            pass


def check_month(month):
    if month.isdigit() and int(month) <= 12:
        return int(month)
    elif month.isalpha() and month.title() in months:
        return months.index(month.title()) + 1
    else:
        raise KeyError


def check_day(day):
    if int(day) >= 1 and int(day) <= 31:
        return int(day)
    else:
        raise ValueError


def check_year(year):
    if len(year) < 4:
        raise ValueError
    else:
        return year


main()
