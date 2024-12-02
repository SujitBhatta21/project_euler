"""
Problem 10: Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below n.
"""

# Returns true if number is prime.
def primeChecker(n):
    for i in range(2, (n//2) + 1):
        if not n % i:
            return False
    return True


def P4():
    sum = 2
    
    for i in range(3, 100000, 2):
        if primeChecker(i):
            sum += i
    return sum


if __name__ == "__main__":
    print("For 200000: ", P4())
