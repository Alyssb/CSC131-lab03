"""
CSC131 - Computational Thinking, Spring 2018
Missouri State University

The purpose of this lab is to practice working with Python's higher order functions and ternary operator.
"""
from functools import reduce # needed for use in question_3()

# Useful named constant used in main()
# http://www.u.arizona.edu/~erdmann/mse350/topics/list_comprehensions.html <- v useful keep link
# http://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php <- this one too
EXIT_SUCCESS = 0


def question_1(a: list) -> list:
    """
    Using the map function and a lambda argument, write an expression that produces a list of the cubes of the
    values in a and return the resulting list.
    :param a: A list of integers used to generate the return value
    :return: A list of cubes of the given list values is returned.
    """

    cube = list(map(lambda x: x**3,a))

    # TODO: Implement me properly.
    return cube


def question_2(a: list) -> list:
    """
    Using the filter function and a lambda argument, write an expression that produces a list of the values in a that
    are divisible by 3 and return the resulting list.
    :param a: A list of integers used to generate the return value
    :return: A list of values filtered out from the given list containing values that are divisible by 3.
    """
    is_divide = list(filter(lambda x: x%3==0,a))

    # TODO: Implement me properly.
    return is_divide


def question_3(a: list) -> str:
    """
    Using the reduce function and a lambda argument, write an expression that returns the result of concatenating all
    the digits in a and return the resulting string. For example, if a = list(range(1, 11)),
    the the return value of this function would be the string '12345678910'
    :param a: A list to reduce as prescribed.
    :return: The string resulting from the concatenation of the digits in the given list.
    """
    conc = reduce(lambda x,y:str(x)+str(y),a)
    # TODO: Implement me properly.
    return conc


def question_4(a: list) -> list:
    """
    Use a list comprehension to produce the same list as in question 1 (i.e., the new list will contain the cubes of the
    values in a). See https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions.
    :param a: A list of integers used to generate the return value
    :return: A list of cubes of the given list values is returned.
    """
    one_again = [x**3 for x in a]
    # TODO: Implement me properly.
    return one_again


def question_5(a: list) -> list:
    """
    Use a list comprehension to produce the same list as in question 2.
    See https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions.
    :param a: A list of integers used to generate the return value
    :return: A list of values filtered out from the given list containing values that are divisible by 3.
    """

    # TODO: Implement me properly.
    return []


def question_6(a: list) -> list:
    """
    Use a list comprehension to produce a list containing the cubes of the values in a that are divisible by 3. For
    example, if a = list(range(1, 11)), then the output from this function would be the list [27, 216, 729].
    See https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions.
    :param a: A list of integers used to generate the return value
    :return: A list containing the cubes of the values in a that are divisible by 3 is returned.
    """
    # TODO: Implement me properly.
    return []


def even_filter(a: dict) -> list:
    """
    With the given dictionary of elements indexed by integer keys and using only a list comprehension, return the values
    of the elements associated with the keys that are evenly divisible by 2. For example,
    if a = {1: "one",  3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"},
    then even_filter(data) = ['four', 'eight', 'ten']
    See https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions.
    :param a: A dictionary indexed by integer keys
    :return: A list of elements associated with the keys that are evenly divisible by 2 is returned.
    """
    # TODO: Implement me properly.
    return []


def find_min(x: int, y: int) -> int:
    """
    Implement this function using the ternary operator (i.e, conditional expression) to find and return the minimum of
    its two arguments. Assume that x and y are numbers.
    :param x: a number used in the comparison
    :param y: another number used in the comparison
    :return: The minimum of the two arguments is returned.
    """
    # TODO: Implement me properly.
    return 0


def main() -> int:
    """
    A "driver program" to see the output of your function implementations.
    :return: EXIT_SUCCESS is returned by successful execution of this function.
    """
    a = list(range(1, 11))

    # Map
    print("Mapping yields:", question_1(a))

    # Filter
    print("Filtering yields:", question_2(a))

    # Reduce
    print("Reduce yields:", question_3(a))

    # List comprehension
    print("Question 4 - list comprehension =", question_4(a))
    print("Question 5 - list comprehension =", question_5(a))
    print("Question 6 - list comprehension =", question_6(a))
    a = {1: "one",  3: "three", 4: "four", 5: "five", 8: "eight", 10: "ten"}
    print("even_filter(a) =", even_filter(a))

    # Ternary conditional operator
    print("find_min(-3, 4) =", find_min(-3, 4))
    print("find_min(4, -3) =", find_min(4, -3))
    print("find_min(4, 4) =", find_min(4, 4))

    return EXIT_SUCCESS


if __name__ == '__main__':
    main()
