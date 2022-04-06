import time


def timer(f, *structure, **structure_keyword):
    start_time = time.time()
    map(f, filter(None, [structure, structure_keyword]))
    return time.time() - start_time


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))
