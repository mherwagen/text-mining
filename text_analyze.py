from thefuzz import fuzz
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def count_words(string):
    """
    Returns number of words in a string.
    """
    return len(string.split())


def remove_stopwords(string):
    """
    Returns string without irrelevant words
    """
    new_string = ''

    f = open('stopwords.txt')
    stopwords = []
    for line in f:
        word = line.strip()
        stopwords.append(word)

    for word in string.split():
        if word in stopwords:
            continue
        new_string += (word + ' ')

    return new_string


def compare(string1, string2):
    """
    Uses fuzz library to return different comparison metrics of two strings, without irrelevant words
    """
    new_string1 = remove_stopwords(string1)
    new_string2 = remove_stopwords(string2)

    compare = fuzz.ratio(new_string1, new_string2)
    partial = fuzz.partial_ratio(new_string1, new_string2)
    sort = fuzz.token_sort_ratio(new_string1, new_string2)
    token_set = fuzz.token_set_ratio(new_string1, new_string2)
    return compare, partial, sort, token_set


def sentiment(string):
    """
    Return sentiment analysis of a string using nltk library.
    """
    sent = SentimentIntensityAnalyzer().polarity_scores(string)
    return sent


def comp_sent(num1, num2):
    """
    Compares two numbers and returns a string to describe the comparison of the second as seen from the first.
    """
    round(num1, 1)
    round(num2, 1)
    if num1 > num2:
        return 'more'
    if num2 > num1:
        return 'less'
    if num1 == num2:
        return 'similarly'


def main():
    count_words()
    remove_stopwords()
    compare()
    sentiment()
    comp_sent()


if __name__ == "__main__":
    main()
