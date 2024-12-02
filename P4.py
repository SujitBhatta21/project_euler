"""
Problem 4: Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two n-digit numbers.
"""
def isPalindrome(num):
    return num == num[::-1]

def P4():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            temp = i * j
            if isPalindrome(str(temp)):
                largest = max(largest, temp)
    return largest



if __name__ == "__main__":
    print(P4())