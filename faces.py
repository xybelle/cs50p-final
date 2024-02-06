def main():
    message = input("Message: ")
    converted_message = convert(message)

    print(converted_message)


def convert(m):
    if ":)" in m:
        m = m.replace(":)", "🙂")
    if ":(" in m:
        m = m.replace(":(", "🙁")
    return m


main()
