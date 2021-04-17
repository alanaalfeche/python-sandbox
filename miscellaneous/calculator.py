print("Welcome to addition land.")
while True:
    statement = input("Enter here: ")
    addends = statement.split("+")
    addends = [addend.strip() for addend in addends]

    all_integer = True
    for addend in addends:
        if '.' in addend:
            all_integer = False

    if all_integer:
        print(sum([int(addend) for addend in addends]))
    else:
        print(sum([float(addend) for addend in addends]))
