
def full_names(first_name_list, last_name_list, min_len=0):
    """
    Combine first and last name and returns the ones that have pass the minimum length.

    :param first_name_list: The list of the first names.
    :param last_name_list: The list of the last names.
    :param min_len: The minimum length of the full name.
    :return: List of all the full names combination that pass the minimum length.
    """
    full_names_list = [first_name.capitalize() + ' ' + last_name.capitalize() for first_name in first_name_list for last_name in last_name_list]
    return list(filter(lambda full_name: len(full_name) >= min_len, full_names_list))


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 14))
    print(full_names(first_names, last_names))
