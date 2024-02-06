q = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().lstrip().removesuffix(" ")
if q == "42" or q == "forty two" or q == "forty-two":
    print("Yes")
else:
    print("No")
