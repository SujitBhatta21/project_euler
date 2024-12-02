"""
Problem 16: Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^exponent?
"""


def P6(exponent):
    temp = 2 ** exponent
    print(temp)
    sum_of_digits = 0
    
    for digit in str(temp):
        sum_of_digits += int(digit)

    return sum_of_digits


if __name__ == "__main__":
    print(P6(1000))


"""
Note:
From line 13 to __ can be summarised by just this line of code.
sum_of_digits = sum(int(digit) for digit in str(temp))
"""