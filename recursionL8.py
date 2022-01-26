# /users/tannerwilliams/desktop/ME 499/ME499_ClassExamples

import random
import math  # Using to test against our functions


def compute_factorial(n):
    """
    compute the factorial of a given number
    :param n: given number
    :return: n!
    """
    if n > 0:  # Recursive case for non-zero factorial
        return n * compute_factorial(n-1)  # if input is 3 then 3 * (3-1) * (3-2) = 6
    else:  # Base case (zero factorial is just 1)
        return 1


def compute_sum(n):
    """
    Compute some of numbers from 1 to n
    :param n: last number
    :return: sum
    """
    if n > 0:
        return n + compute_sum(n-1)  # if input is 3 then 3 + (3-1) + (3-2) = 6
    else:
        return 0  # Base case (sum of all number from 0 to n=0 is 0)


def recursive_print(A):
    """
    Recursively print a list by popping elements and using a nested recursion
    :param A: given list
    :param B:
    :return:
    """
    B = A.copy()  # Making a copy of list 'A' so we don't alter it

    def nested_print(B):  # nested function
        print(B.pop(0))  # print first element
        # nested_print(B)  # print each element as before it erases that element
        nested_print(B[1:])  # prints each element and doesn't erase that element


def sum_a_list(A):
    """
    Returns sum of a list
    :param A: given list
    :return: sum of A
    """


def find_letter(word, letter):
    """
    Find a letter in a word with a binary search
    :param word:
    :param letter:
    :return:
    """
    # # find if there is an 'e' (case-specific) in a word
    # if word != "":  # as long as word is not an empty string
    #     return letter == word[0] or find_letter(word[1:], letter)
    # else:
    #     return False

    w1 = len(word)  # int representing length of word
    if w1 > 1:  # as long as word is longer than one letter
        first_half = find_letter(word[w1//2], letter)  # checking first half of word
        second_half = find_letter(word[:w1//2], letter)  # checking second half of word
        return first_half or second_half
    else:
        return letter == word


if __name__ == "__main__":

    print('6! = ', compute_factorial(6))

    # 100 examples testing against our custom factorial function
    for i in range(100):
        n = random.randint(0, 20) # get random int each time
        assert compute_factorial(n) == math.factorial(n)  # test each number in each function

    test_list = [1, 'b', 8, '4']
    recursive_print(test_list)
    print(test_list)

    # print('# of (e) in Hello = ', find_letter('Hello', 'e'))

    # # Testing random word and letters
    # print('# of letters in word = ', find_letter('TannerWilliams', 'n'))
    # ran_char = lambda: char(random.randint(48, 126))
    # for i in range (10):
    #     word = "".join([ran_char() for i in range(10)])
    #     letter = ran_char()
    #     if find_letter(word, letter) > 1:
    #         return

