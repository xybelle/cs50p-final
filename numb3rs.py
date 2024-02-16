import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if valid := re.search(r"^((25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]?[0-9])$", ip):
        if four_sets(ip):
            return True
    else:
        return False


def four_sets(n):
    n = n.split(".")
    if len(n) != 4:
        return False
    return True


if __name__ == "__main__":
    main()
