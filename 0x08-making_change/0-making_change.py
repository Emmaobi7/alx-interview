#!/usr/bin/python3
"""
change comes from within
"""


def makeChange(coins, total):
    """
    makeChange: fewest number of coins to reach total
    implemetation: using greedy algorithm
    return: number of fewest coins
    """
    if total <= 0:
        return 0

    ans = []
    n = len(coins)
    i = n - 1
    while(i >= 0):
        while(total >= coins[i]):
            total -= coins[i]
            ans.append(coins[i])
        i -= 1
    if total > 0:
        return -1
    return len(ans)
