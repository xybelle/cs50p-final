amount_due, c = 50, 0
valid_c = [25, 10, 5]

while True:
    print(f"Amount due: {amount_due}\n")
    c = int(input("Insert coin: "))
    if c not in valid_c:
        continue
    else:
        amount_due -= c
        if amount_due <= 0:
            break
change = abs(amount_due)
print(f"Change owed: {change}")
