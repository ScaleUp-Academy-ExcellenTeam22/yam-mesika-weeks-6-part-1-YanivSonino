def my_filter(function, structure):
    """

    :param function: The function you want to apply on every item in the structure
    :param structure: The structure you want to apply the filter
    :return: list of filtered structure
    """
    return [item for item in structure if function(item)]


if __name__ == '__main__':
    print(my_filter(lambda x: x > 3, range(1, 10)))
