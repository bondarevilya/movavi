
cost = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}


basket = {
    'banana': 2,
    'orange' : 2,
    'apple' : 1,
    'pear' : 2
}


def command_bill (cost, basket):
    res = {}
    for key in basket.keys():
        res[key] = basket[key] * cost[key]
    return res


summ=command_bill (cost, basket)
print(summ)