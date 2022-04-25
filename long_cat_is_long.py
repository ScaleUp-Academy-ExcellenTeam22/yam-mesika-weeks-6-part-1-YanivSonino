def count_words(text_to_count):
    """
    Counts the length of every word.

    :param text_to_count: The text you want to count.
    :return: Dictionary of words and their length
    """
    list_of_words = [word.strip(",.?:") for word in text_to_count.split()]
    return {word: len(word) for word in list_of_words}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
