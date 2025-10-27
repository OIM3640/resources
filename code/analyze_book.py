import random
import string
import sys
from collections import Counter
from unicodedata import category


def process_file(filename, skip_header=True):
    """Makes a histogram that counts the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    """
    hist = {}

    # Unicode punctuation characters. Ref: https://stackoverflow.com/a/60983895
    STRIPPABLES = "".join(
        chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")
    )

    with open(filename, encoding="utf-8") as f:
        # Skip Gutenberg header if needed
        if skip_header:
            for line in f:
                if "START OF THE PROJECT" in line.upper():
                    break

        # Process content
        for line in f:
            if line.startswith("*** END OF THE PROJECT"):
                break

            # Replace dashes with spaces
            line = line.replace("-", " ").replace(chr(8212), " ")

            # Extract and clean words
            for word in line.split():
                word = word.strip(STRIPPABLES).lower()
                hist[word] = hist.get(word, 0) + 1

    return hist


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
