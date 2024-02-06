a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").casefold().replace(" ", "")
if a == "42" or a == "forty two" or a == "forty-two":
    print("Yes")
else:
    print("No")
