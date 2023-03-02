from pronounce import read_dictionary


def make_word_dict():
    """Read. the words in words.txt and return a dictionary
    that contains the words as keys."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d


def homophones(a, b, phonetic):
    """Checks if words two can be pronounced the same way.

    If either word is not in the pronouncing dictionary, return False

    a, b: strings
    phonetic: map from words to pronunciation codes
    """


def check_word(word, word_dict, phonetic):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.

    word: string
    word_dict: dictionary with words as keys
    phonetic: map from words to pronunciation codes
    """


if __name__ == '__main__':
    phonetic = read_dictionary()
    word_dict = make_word_dict()

    for word in word_dict:
        if check_word(word, word_dict, phonetic):
            print(word, word[1:], word[0] + word[2:])
