import emoji

a = input("Input: ")
print("Output: ", end="")

print(emoji.emojize(f"{a}", language='alias'))
