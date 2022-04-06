def full_names(first_name_list, last_name_list, min_len=0):
    return \
        [first_name.capitalize() + ' ' + last_name.capitalize()
         for first_name in first_name_list
         for last_name in last_name_list
         if len(first_name + ' ' + last_name) >= min_len]


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']
    print(full_names(first_names, last_names, 14))
    print(full_names(first_names, last_names))