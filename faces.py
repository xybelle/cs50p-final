def main():
    message = input("Message: ")
    converted_message = convert(message)

    print(converted_message)


def convert(m):
    if ":)" in m:
        new_m = m.replace(":)", "🙂")
    if ":(" in m:
        new_m = new_m.replace(":(", "🙁")
    return new_m


main()
