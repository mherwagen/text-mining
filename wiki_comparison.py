from mediawiki import MediaWiki
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from regex import F
from thefuzz import fuzz


def access_data():
    """
    Access Wikipedia pages for Johnny Depp and Amber Heard and write the content into text files.
    """
    wikipedia = MediaWiki()

    jd = wikipedia.page("Johnny Depp")
    ah = wikipedia.page("Amber Heard")
    text_file = open('johnny_depp.txt', 'w', encoding="utf-8")
    text_file.write(jd.content)
    text_file.close()

    text_file = open('amber_heard.txt', 'w', encoding="utf-8")
    text_file.write(ah.content)
    text_file.close()


def read_part(file, start_string, end_string):
    """
    return part of a text file between specified lines (start and end strings) as a string
    file: .txt
    start_string, end_string: string
    """
    res = ''  # Array for saving lines
    f = open(file, 'r', encoding="utf-8")
    for line in f:
        lines = f.read()
        # credit for searching between two points of a string: https://stackoverflow.com/a/55917313
        lines = lines[lines.find(start_string):lines.find(end_string)]
        res += lines
    return res


def compare(string1, string2):
    """
    Uses fuzz library to return different comparison metrics of two strings
    """
    compare = fuzz.ratio(string1, string2)
    partial = fuzz.partial_ratio(string1, string2)
    sort = fuzz.token_sort_ratio(string1, string2)
    token_set = fuzz.token_set_ratio(string1, string2)
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
    access_data()

    print('Below is analysis of Johnny Depp and Amber Heard\'s Wikipedia pages with a focus on their career and personal life sections.')
    print()

    jd_career = read_part(
        'johnny_depp.txt', '== Career ==', '== Other ventures ==')
    ah_career = read_part('amber_heard.txt', '== Career ==',
                          '== Charity and activism ==')

    career_comp = compare(jd_career, ah_career)
    print(
        f'The career sections about Johnny Depp and Amber Heard compare at indexes of {career_comp} out of 100 possible for closest matches. These numbers describe the Levenshtein Distances between the entries as assessed by different ratios with increasing levels of leniency towards repetition and shuffle.')
    print()

    jd_career_sent = sentiment(jd_career)
    ah_career_sent = sentiment(ah_career)
    print(
        f"Sentiment analysis for Johnny Depp\'s career section shows that {jd_career_sent['neg']*100:.2f}% of the entry is negative, {jd_career_sent['pos']*100:.2f}% is positive, and the remaining {jd_career_sent['neu']*100:.2f}% is neutral.")
    print(
        f"Sentiment analysis for Amber Heard\'s career section shows that {ah_career_sent['neg']*100:.2f}% of the entry is negative, {ah_career_sent['pos']*100:.2f}% is positive, and the remaining {ah_career_sent['neu']*100:.2f}% is neutral.")
    print(
        f"Sentiment analysis shows that Johnny Depp\'s career section is {comp_sent(jd_career_sent['neg'],ah_career_sent['neg'])} negative, {comp_sent(jd_career_sent['pos'],ah_career_sent['pos'])} positive, and {comp_sent(jd_career_sent['neu'],ah_career_sent['neu'])} neutral than Amber Heard\'s.")
    print()

    jd_pl = read_part('johnny_depp.txt', '== Personal life ==',
                      '== Filmography and accolades ==')
    ah_pl = read_part('amber_heard.txt',
                      '== Personal life ==', '== Filmography ==')

    pl_comp = compare(jd_pl, ah_pl)
    print(
        f'The personal life sections about Johnny Depp and Amber Heard, which both include the trial, compare at indexes of {pl_comp} out of 100 possible for closest matches. These numbers describe the Levenshtein Distances between the entries as assessed by different ratios with increasing levels of leniency towards repetition and shuffle.')
    print()

    jd_pl_sent = sentiment(jd_pl)
    ah_pl_sent = sentiment(ah_pl)
    print(
        f"Sentiment analysis for Johnny Depp\'s personal section shows that {jd_pl_sent['neg']*100:.2f}% of the entry is negative, {jd_pl_sent['pos']*100:.2f}% is positive, and the remaining {jd_pl_sent['neu']*100:.2f}% is neutral.")
    print(
        f"Sentiment analysis for Amber Heard\'s personal life section shows that {ah_pl_sent['neg']*100:.2f}% of the entry is negative, {ah_pl_sent['pos']*100:.2f}% is positive, and the remaining {ah_pl_sent['neu']*100:.2f}% is neutral.")
    print(
        f"Sentiment analysis shows that Johnny Depp\'s personal life section is {comp_sent(jd_pl_sent['neg'],ah_pl_sent['neg'])} negative, {comp_sent(jd_pl_sent['pos'],ah_pl_sent['pos'])} positive, and {comp_sent(jd_pl_sent['neu'],ah_pl_sent['neu'])} neutral than Amber Heard\'s.")


if __name__ == '__main__':
    main()
