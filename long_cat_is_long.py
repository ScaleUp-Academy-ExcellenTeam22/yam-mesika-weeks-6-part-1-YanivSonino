import string


def count_words(text_to_count):
    new_word = ''
    list_of_words = []
    # generator to find all the letters and spaces
    pure_text = (letter for letter in text_to_count if letter.isalpha() or letter.isspace())
    for letter in pure_text:
        if letter.isalpha():
            new_word += letter
        if letter.isspace():
            if new_word == '':
                continue
            else:
                list_of_words.append(new_word)
                new_word = ''

    return {word: len(word) for word in list_of_words}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    dict_of_words = count_words(text)
    print(dict_of_words)
