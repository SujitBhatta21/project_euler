"""
Problem 31: Coin sums

NOTE: This is Dynamic Programming Question.

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can n pence be made using any number of coins?
"""

def P7(n):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (n + 1)
    ways[0] = 1
    
    # ways[i - coin] contains number of times i can be made using coins visited until now. So, ways[i] += ways[i-coin] 
    # So, when i == 200 loop ends and we print last index of array ways.
    for coin in coins:
        for i in range(coin, n + 1):
            # DP becaue: E.g. i = 2 (range is 2 to 5(technically 6))
            # ways[2] = 1 + ways[0] = 1 + 1 = 2
            # ...
            # ways[4] = 1 + ways[4 - 2] = 1 + ways[2]
            # So, ways[4] needs ways[2] value and ways[2] val was updated on same iteration.
            ways[i] += ways[i - coin]
    
    return ways[n]

if __name__ == "__main__":
    print(P7(200))
