grocery_list = {}
while True:
    try:
        item = input()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        ls = sorted(grocery_list.keys())
        for item in ls:
            print(f"{grocery_list.get(item)} {item.upper()}")
        break
