import inflect

p = inflect.engine()

names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        print("Adiue, adieu, to ", end="")
        a = p.join(names)
        print(a)
        break
