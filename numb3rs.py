import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if valid := re.search(r"([0-2]?[0-9]?[0-9]?\.){3}[0-2]?[0-9]?[0-9]?", ip):
        if max_255(ip):
            return True
    return False


def max_255(digits):
    parts = digits.split(".")
    if len(parts) > 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
            break
        if int(part) > 255:
            return False
            break
    return True


if __name__ == "__main__":
    main()
