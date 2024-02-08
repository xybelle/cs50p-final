vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
s = input("Input: ")

for c in s:
    if c in vowels:
        continue
    print(c, end="")
print()
