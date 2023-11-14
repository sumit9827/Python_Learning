import sys
from urllib.request import urlopen

def fetch_words():
    story = urlopen('http://sixty-north.com/c/t.txt')
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for words in line_words:
            story_words.append(words)
    story.close()
    return story_words


    def print_items(items):
        for item in items:
            print(item)

def main(url):
    words = fetch_words(url)
    print(words)


if __name__ == '__main__':
    main(sys.argv[1])    