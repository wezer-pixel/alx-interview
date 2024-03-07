#!/usr/bin/python3

""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet the total.
    
    Args:
        coins (list): A list of coin denominations.
        total (int): The target total amount.
    
    Returns:
        int: The fewest number of coins needed to meet the total. Returns -1 if the total cannot be met.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if total == 0:
            return change
    return -1
