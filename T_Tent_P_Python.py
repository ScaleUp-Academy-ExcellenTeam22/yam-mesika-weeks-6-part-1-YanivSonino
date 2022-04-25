def get_letter():
    """
    Get all the letters in the English Alphabet.

    :return: List of the English Alphabet.
    """
    return [chr(letter) for letter in range(ord('A'), ord('z') + 1) if letter <= ord('Z') or letter >= ord('a')]


if __name__ == '__main__':
    print(get_letter())
