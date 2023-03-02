def make_word_dict():
    """Reads a word list and returns a dictionary."""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None

    # have to add single letter words to the word list;
    # also, the empty string is considered a word.
    for letter in ['a', 'i', '']:
        d[letter] = letter
    return d


"""memo is a dictionary that maps from each word that is known
to be reducible to a list of its reducible children.  It starts
with the empty string."""

memo = {}
memo[''] = ['']


def is_reducible(word, word_dict):
    """If word is reducible, returns a list of its reducible children.

    Also adds an entry to the memo dictionary.

    A string is reducible if it has at least one child that is 
    reducible.  The empty string is also reducible.

    word: string
    word_dict: dictionary with words as keys
    """
    # if have already checked this word, return the answer

    # check each of the children and make a list of the reducible ones

    # memoize and return the result


def children(word, word_dict):
    """Returns a list of all words that can be formed by removing one letter.

    word: string

    Returns: list of strings
    """


def all_reducible(word_dict):
    """Checks all words in the word_dict; returns a list reducible ones.

    word_dict: dictionary with words as keys
    """


def print_trail(word):
    """Prints the sequence of words that reduces this word to the empty string.

    If there is more than one choice, it chooses the first.

    word: string
    """


def print_longest_words(word_dict):
    """Finds the longest reducible words and prints them.

    word_dict: dictionary of valid words
    """
    words = all_reducible(word_dict)

    # use DSU to sort by word length

    # print the longest 5 words


if __name__ == '__main__':
    word_dict = make_word_dict()
    print_longest_words(word_dict)
