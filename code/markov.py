import sys
import random
from unicodedata import category

# global variables
suffix_map = {}  # map from prefixes to a list of suffixes
prefix = ()  # current tuple of words


def process_file(filename, order=2):
    """Reads a file and performs Markov analysis.

    filename: string
    order: integer number of words in the prefix

    returns: map from prefix to list of possible suffixes.
    """
    fp = open(filename, encoding="utf8")

    skip_gutenberg_header(fp)

    # strippables = string.punctuation + string.whitespace
    # via: https://stackoverflow.com/questions/60983836/complete-set-of-punctuation-marks-for-python-not-just-ascii

    strippables = "".join(
        [chr(i) for i in range(sys.maxunicode) if category(chr(i)).startswith("P")]
    )

    for line in fp:
        if line.startswith("*** END OF THIS PROJECT"):
            break

        line = line.replace("-", " ")
        line = line.replace(
            chr(8212), " "
        )  # Unicode 8212 is the HTML decimal entity for em dash

        for word in line.split():
            # remove punctuation and convert to lowercase
            word = word.strip(strippables)
            word = word.lower()
            process_word(word, order)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith("*** START OF THIS PROJECT"):
            break


def process_word(word, order=2):
    """Processes each word.

    word: string
    order: integer

    During the first few iterations, all we do is store up the words;
    after that we start adding entries to the dictionary.
    """
    global prefix
    if len(prefix) < order:
        prefix += (word,)
        return

    try:
        suffix_map[prefix].append(word)
    except KeyError:
        # if there is no entry for this prefix, make one
        suffix_map[prefix] = [word]

    prefix = shift(prefix, word)


def random_text(n=100):
    """Generates random wordsfrom the analyzed text.

    Starts with a random prefix from the dictionary.

    n: number of words to generate
    """
    # choose a random prefix (not weighted by frequency)
    start = random.choice(list(suffix_map.keys()))

    for i in range(n):
        suffixes = suffix_map.get(start, None)
        if suffixes is None:
            # if the start isn't in map, we got to the end of the
            # original text, so we have to start again.
            random_text(n - i)
            return

        # choose a random suffix
        word = random.choice(suffixes)
        print(word, end=" ")
        start = shift(start, word)


def shift(t, word):
    """Forms a new tuple by removing the head and adding word to the tail.

    t: tuple of strings
    word: string

    Returns: tuple of strings
    """
    return t[1:] + (word,)


def main():
    filename = "data/Pride and Prejudice.txt"
    process_file(filename, 2)
    random_text(100)


if __name__ == "__main__":
    main()
