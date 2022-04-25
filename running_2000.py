import time


def timer(function, *structure, **structure_keyword):
    """
    Count the time that the function took to work over the structure.

    :param function: The function we want to measure.
    :param structure: The iterable structure we want to check.
    :param structure_keyword: The key structure we want to check.
    :return: The time took to finish the function.
    """
    start_time = time.time()
    map(function, filter(None, [structure, structure_keyword]))
    return time.time() - start_time


if __name__ == '__main__':
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print(timer("Hi {name}".format, name="Bug"))
