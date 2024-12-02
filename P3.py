"""
Problem 9: Special Pythagorean triplet
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc such that a + b + c = n.
"""

def P3():
    # Lower limit of c is 334 can't be 333 or below.
    # Upper limit of c is 499 else a + b > 500. 
    for c in range(334,500):
        for a in range(1, int((1000-c)/2)):
            b = (1000 - c) - a
            if a**2 + b**2 == c**2:
                return a*b*c


if __name__ == "__main__":
    print(P3())