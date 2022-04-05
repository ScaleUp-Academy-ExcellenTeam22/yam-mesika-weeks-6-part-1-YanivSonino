def get_positive_numbers():
    return tuple(
        filter(lambda n: n > 0,  # filter positive numbers
               map(lambda n: int(n),  # casting all elements in list to int
                   input("enter list of numbers seperate by ',': ").split(
                       ','))))  # gets string from the user and create a list seperate by ','


print(get_positive_numbers())
