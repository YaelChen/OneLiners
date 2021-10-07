# One Liners using regular functions:


def comb(num):
    """
    combines a number and the sign "$" to one string.
    :param num: a given number
    :type num: int
    :return: a string of the given number and the sign "$"
    :rtype: str
    """
    return str(num) + "$"


def mult(a, b):
    """
    Multiplying two given numbers.
    :param a: a given number
    :param b: a given number
    :type a: int
    :type b: int
    :return: the multiplication of a and b
    :rtype: int
    """
    return a * b


def combine_coins(number, coin):
    """
    takes any list of numbers and returns an str of the numbers with coin sign.
    :param coin: a sign of a coin
    :param number: a list of numbers to join to the coin sign
    :type coin: str
    :type number: list, range
    :return coin_list: an updated list
    :rtype coin_list: a list joined to str
    """
    return str(number) + coin


print(", ".join(list(map(comb, range(1, 8)))))
print(list(map(mult, range(1, 5), range(1, 7))))
print(", ".join(list(map(combine_coins, range(5), ["$"] * 5))))

print("\n--- One Liners ---")  # One Liners using lambda:

print(", ".join(list(map((lambda x: str(x)+"$"), range(1, 8)))))
print(list(map((lambda x, y: x * y), range(1, 5), range(1, 7))))
print(", ".join([str(coin) + "$" for coin in range(5)]))
