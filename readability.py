from cs50 import get_string


def main():
    # Prompt user for some text
    txt = get_string("Text: ")

    # Compute total number of letters, words, and sentences in the text
    letters = count_letters(txt)
    words = count_words(txt)
    sentences = count_sentences(txt)

    # Compute the Coleman-Liau index
    L = 100.0 * letters / words
    S = 100.0 * sentences / words
    index = 0.0588 * L - 0.296 * S - 15.8

    # Print the grade level
    if round(index) >= 16:
        print("Grade 16+")
    elif round(index) < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {int(round(index))}")


def count_letters(txt):
    return sum(c.isalpha() for c in txt)


def count_words(txt):
    words = txt.split()
    return len(words)


def count_sentences(txt):
    sentence_endings = ['.', '!', '?']
    cs = 0
    for char in txt:
        if char in sentence_endings:
            cs += 1

    return cs


main()
