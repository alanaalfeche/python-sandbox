def atm(withdraw):
    result = {}
    denominations = [1, 2, 5, 10, 20, 50, 100]
    for i in range(len(denominations)-1, -1, -1):
        while (withdraw - denominations[i]) >= 0:
            if denominations[i] not in result:
                result[denominations[i]] = 1 
            else:
                result[denominations[i]] += 1
            withdraw = withdraw - denominations[i]

atm(110)

    