from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

# Get's the URL text information
text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt')\
               .text


def get_text(url):
    """
    Article Information.

    return a summarization of the article title and content. The reason we use
    beautifulsoup4 here, is so that we get only the text in the page and not
    everything else. So in summart the third line looks for all the p tags
    in the html page and then creates a summarization from that information.
    """
    page = urlopen(url)
    soup = BeautifulSoup(page, "lxml")
    text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return soup.title.text, text


# This will use the first URL "matrix script" and returns a sumization of the
# information. ratio is the length of the summarization of the content.
print('\n\nSummary:')
print(summarize(text, ratio=0.01))


url = "https://en.wikipedia.org/wiki/Deep_learning"
text = get_text(url)

print('\n\nSummary:')
print(summarize(str(text), ratio=0.02))
