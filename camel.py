s = input("camelCase: ")

for c in s:
    if c.isupper():
        print(f"_{c.lower()}", end="")
        continue
    print(c, end="")
print()
