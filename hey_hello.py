def words_length(sentence):
    return [len(word) for word in sentence]


if __name__ == '__main__':
    size_words_list = words_length(list(input("Enter sentence\n").split()))
    print(size_words_list)
