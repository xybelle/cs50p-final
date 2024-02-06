amount_due, c = 50, 0
valid_c = [25, 10, 5]

while True:
    print(f"Amount Due: {amount_due}")
    c = int(input("Insert coin: "))
    if c not in valid_c:
        continue
    else:
        amount_due -= c
        if amount_due <= 0:
            break
change = abs(amount_due)
print(f"Change Owed: {change}")
