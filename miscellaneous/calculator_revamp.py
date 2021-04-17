print('Welcome to Addition Land.')
while True:
    statement = input('input> ')
    addends = [addend.strip() for addend in statement.split('+')]
    print(sum(map(float if any('.' in addend for addend in addends) else int, addends)))
