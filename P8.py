"""
Problem 6: Sum square difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first n natural numbers and the square of the sum.
"""

def sum_of_squares(n):
    answer = 0
    while n > 0:
        answer += n**2
        n -= 1
    return answer


def square_of_sum(n):
    answer = 0
    while n > 0:
        answer += n
        n -= 1
    return answer**2


if __name__ == "__main__":
    a =  square_of_sum(100)
    b = sum_of_squares(100)
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'answer: {a-b}')