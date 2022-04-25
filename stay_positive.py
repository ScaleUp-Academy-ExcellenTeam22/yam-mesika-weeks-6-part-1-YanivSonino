def get_positive_numbers():
    """
    Gets list of numbers from the user and finds the positive numbers.

    :return: Tuple of positive numbers.
    """
    list_of_numbers = input("enter list of numbers seperate by ',': ").split(',')  # gets string from the user
    return tuple(filter(lambda n: n > 0, map(lambda number: int(number), list_of_numbers)))


if __name__ == '__main__':
    print(get_positive_numbers())
