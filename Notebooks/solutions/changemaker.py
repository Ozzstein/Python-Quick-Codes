
def make_change(dollars, cents):
    """
    Returns a list of coin values that make up $dollars.cents
    Example:

    >>> make_change(4, 25)
    [200, 200, 20, 5]

    >>> make_change(1, 95)
    [100, 50, 20, 20, 5]
    """
    COINS = [200, 100, 50, 20, 10, 5]
    orig_value = dollars * 100 + cents
    value = orig_value
    change = []
    i = 0
    while i < len(COINS):
        coin = COINS[i]
        if value >= coin:
            change.append(coin)
            value -= coin
        else:
            i += 1
    assert sum(change) == dollars * 100 + cents
    return change

print(make_change(3, 95))
print(make_change(5, 10))
print(make_change(0, 25))
