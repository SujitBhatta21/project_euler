"""
Problem 36: Double-base palindromes
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than n, whereas 1000 ≤ n ≤ 1000000, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def isPalindrome(number):
    number = str(number)
    return number == number[::-1]

def isBinaryPalindrome(number):
    binary_str = bin(number)[2:]
    return binary_str == binary_str[::-1]


def P10():
    sum = 0
    for i in range(1000000):
        if isPalindrome(i):
            # Check its binary for palindrome.
            if isBinaryPalindrome(i):
                sum += i

    return sum



if __name__ == "__main__":
    print(P10())

