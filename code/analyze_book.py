import random
import string
import sys
from unicodedata import category


def process_file(filename, skip_header):
    """Makes a histogram that counts the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}
    fp = open(filename, encoding="utf-8")

    if skip_header:
        skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    strippables = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )  # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895

    for line in fp:
        if line.startswith("*** END OF THE PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(chr(8212), " ")  # Em dash replacement

        for word in line.split():
            word = word.strip(strippables)
            word = word.lower()

            hist[word] = hist.get(word, 0) + 1

    fp.close()
    return hist


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    start_marker = "START OF THE PROJECT"

    for line in fp:
        if start_marker.lower() in line.lower():  # Case-insensitive search
            return
    # If the loop completes without finding the start marker
    raise ValueError(f"Header end marker '{start_marker}' not found in file.")


def total_words(hist):
    """Returns the total of the frequencies in a histogram."""


def different_words(hist):
    """Returns the number of different words in a histogram."""


def most_common(hist, excluding_stopwords=False):
    """Makes a list of word-freq pairs in descending order of frequency.

    hist: map from word to frequency

    returns: list of (frequency, word) pairs
    """


def print_most_common(hist, num=10):
    """Prints the most commons words in a histgram and their frequencies.

    hist: histogram (map from word to frequency)
    num: number of words to print
    """
    pass


def subtract(d1, d2):
    """Returns a dictionary with all keys that appear in d1 but not d2.

    d1, d2: dictionaries
    """
    pass


def random_word(hist):
    """Chooses a random word from a histogram.

    The probability of each word is proportional to its frequency.
    """
    pass


def main():
    # This text file is downloaded from gutenberg.org (https://www.gutenberg.org/cache/epub/1342/pg1342.txt)
    hist = process_file("data/Pride and Prejudice.txt", skip_header=True)

    # print(hist)
    # print(f"Total number of words: {total_words(hist)}")
    # print(f"Number of different words: {different_words(hist)}")

    # t = most_common(hist, excluding_stopwords=True)
    # print("The most common words are:")
    # for freq, word in t[0:20]:
    #     print(word, "\t", freq)

    # words = process_file("words.txt", skip_header=False)

    # diff = subtract(hist, words)
    # print("The words in the book that aren't in the word list are:")
    # for word in diff.keys():
    #     print(word, end=" ")

    # print("\n\nHere are some random words from the book")
    # for i in range(100):
    #     print(random_word(hist), end=" ")


if __name__ == "__main__":
    main()
