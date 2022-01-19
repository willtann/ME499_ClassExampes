# /users/tannerwilliams/desktop/ME 499/ME499_ClassExamples
import random
import operator

if __name__ == '__main__':
    print('Hola Amigo')

# Creating a short list
short_list = [1, 2, 3, 4]
print('short_list =', short_list)

# Transforming a tuple into a list
tuple_to_list = list((1, 2, 3, 4))
print('tuple_to_list =', tuple_to_list)

# Creating a long list
long_list = []
for i in range(10):
    long_list.append(i + random.randint(0, 9))
print('long_list =', long_list)

# Adding to a list (ERROR)
add_this = 5
short_list.append(add_this)
print('add_to_list', short_list)

# Clearing list
clear_this_list = [1, 2, 3]
clear_this_list.clear()
print('cleared list =', clear_this_list)

# Retrieving part of a list (slicing)
first_two_of_short_list = short_list[:2]
print('Retrieved first_two of short_list = ', first_two_of_short_list)


def ex_func(a, b, c):
    """

    :param a: FIRST VARIABLE
    :param b: SECOND VARIABLE
    :param c: THIRD VARIABLE
    :return: ALL GOOD
    """
