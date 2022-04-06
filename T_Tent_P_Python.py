def get_letter():
    return [chr(letter) for letter in range(ord('A'), ord('z')+1) if letter <= ord('Z') or letter >= ord('a')]


if __name__ == '__main__':
    letter_list = get_letter()
    print(letter_list)
