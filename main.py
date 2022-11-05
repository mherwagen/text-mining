from mediawiki import MediaWiki
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from regex import F
from thefuzz import fuzz

from access import access_data, read_part
from text_analyze import count_words, remove_stopwords, compare, sentiment, comp_sent


def main():
    access_data()

    print('Below is analysis of Johnny Depp and Amber Heard\'s Wikipedia pages with a focus on their career and personal life sections.')
    print()

    jd_career = read_part(
        'johnny_depp.txt', '== Career ==', '== Other ventures ==')
    ah_career = read_part('amber_heard.txt', '== Career ==',
                          '== Charity and activism ==')

    jd_career_count = count_words(jd_career)
    ah_career_count = count_words(ah_career)
    print(
        f'Johnny Depp\'s Wikipedia page "Career" section consists of {jd_career_count} words.')
    print(
        f'Amber Heard\'s Wikipedia page "Career" section consists of {ah_career_count} words.')
    print()

    career_comp = compare(jd_career, ah_career)
    # credit for printing tuple without parentheses: https://bobbyhadz.com/blog/python-print-tuple-without-parenthesis
    career_comp = ', '.join(str(number) for number in career_comp)
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

    jd_pl_count = count_words(jd_pl)
    ah_pl_count = count_words(ah_pl)
    print(
        f'Johnny Depp\'s Wikipedia page "Personal Life" section consists of {jd_pl_count} words.')
    print(
        f'Amber Heard\'s Wikipedia page "Personal Life" section consists of {ah_pl_count} words.')
    print()

    pl_comp = compare(jd_pl, ah_pl)
    pl_comp = ', '.join(str(number) for number in pl_comp)
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
