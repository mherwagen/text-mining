from mediawiki import MediaWiki

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

def main():
    access_data()
    read_part()

if __name__ == "__main__":
    main()
