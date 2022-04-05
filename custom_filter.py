def my_filter(func, structure):
    lst = []
    for i in structure:
        if func(i):
            lst.append(i)
    return lst
