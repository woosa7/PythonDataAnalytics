"""
Software Engineering for Data Scientists
"""
# -----------------------------------------------------------------
# Package
# -----------------------------------------------------------------
# directory structure

my_package
    L __init__.py
    L utils.py      :: (fuction) plot_counter, sum_counters
    L document.py   :: (Class) Document

my_script.py
setup.py

# -----------------------------------------------------------------
# import functions in __init__.py

from .utils import plot_counter, sum_counters
from .document import Document, SocialMedia

# -----------------------------------------------------------------
# document.py

class Document:
    def __init__(self, text):
        self.text = text
        self.tokens = self._tokenize()
        self.word_counts = self._count_words()

    def _tokenize(self):
        return tokenize(self.text)

    def _count_words(self):
        return Counter(self.tokens)


class SocialMedia(Document):
    def __init__(self, text):
        Document.__init__(self, text)
        self.hashtag_counts = self._count_hashtags()
        self.mention_counts = self._count_mentions()

    def _count_hashtags(self):
        return filter_word_counts(self.word_counts, first_char='#')

    def _count_mentions(self):
        return filter_word_counts(self.word_counts, first_char='@')

# -----------------------------------------------------------------
# working in my_script.py

import my_package

word_count_totals = my_package.sum_counters(word_counts)

my_package.plot_counter(word_count_totals)
help(my_package.plot_counts)

my_document = my_package.Document(text=datacamp_tweet)
print(datacamp_doc.tokens)
print(datacamp_doc.word_counts.most_common(5))

dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)
print(dc_tweets.mention_counts.most_common(5))

my_package.plot_counter(dc_tweets.hashtag_counts)

# -----------------------------------------------------------------
# requirements.txt

requirements = """
matplotlib>=3.0.0
numpy==1.15.4
pandas<=0.22.0
pycodestyle
"""

# -----------------------------------------------------------------
# install all requirements

pip install -r requirements.txt

# -----------------------------------------------------------------
# setup.py

from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='Perform and visualize a text anaylsis.',
      author='datacamp',
      packages=['my_package'],
      install_requires=['matplotlib>=3.0.0'])

# -----------------------------------------------------------------
