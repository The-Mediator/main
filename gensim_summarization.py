from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt')\
               .text


def get_text(url):
    """
    Article Information.

    return the title and the text of the article
    at the specified url
    """
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text


print('\n\nSummary:')
print(summarize(text, ratio=0.01))


url = "https://en.wikipedia.org/wiki/Deep_learning"
text = get_text(url)

print('\n\nSummary:')
print(summarize(str(text), ratio=0.01))
