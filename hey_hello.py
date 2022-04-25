def words_length(sentence):
    """
    Create list of the length of every word in a sentence.
    :param sentence: The sentence we want to find his words length.
    :return: list of words length.
    """
    return [len(word) for word in sentence]


if __name__ == '__main__':
    size_words_list = words_length(list(input("Enter sentence\n").split()))
    print(size_words_list)
