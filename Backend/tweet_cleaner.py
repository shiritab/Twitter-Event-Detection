# taken from https://github.com/kevalmorabia97/pyTweetCleaner/blob/master/pyTweetCleaner.py
import re
import pandas as pd
from tqdm.auto import tqdm
import json
import datetime
import os
from pathlib import Path
import string
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk
import re
class TweetCleaner:
    def __init__(self, remove_stop_words=False, remove_retweets=False, stopwords_file='NLTK_DEFAULT'):
        """
        clean unnecessary twitter data
        remove_stop_words = True if stopwords are to be removed (default = False)
        remove_retweets = True if retweets are to be removed (default = False)
        stopwords_file = file containing stopwords(one on each line) (default: nltk english stopwords)
        """

        if remove_stop_words:
            if stopwords_file == 'NLTK_DEFAULT':
                self.stop_words = set(stopwords.words('english'))
            else:
                stop_words = set()
                with open(stopwords_file, 'r') as f:
                    for line in f:
                        line = line.replace('\n', '')
                        stop_words.add(line.lower())
                    self.stop_words = stop_words
        else:
            self.stop_words = set()

        self.remove_retweets = remove_retweets

        self.punc_table = str.maketrans("", "", string.punctuation)  # to remove punctuation from each word in tokenize

    def compound_word_split(self, compound_word):
        """
        Split a given compound word(string) and return list of words in given compound_word
        Ex: compound_word='pyTWEETCleaner' --> ['py', 'TWEET', 'Cleaner']
        """
        matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', compound_word)
        return [m.group(0) for m in matches]

    def remove_non_ascii_chars(self, text):
        """
        return text after removing non-ascii characters i.e. characters with ascii value >= 128
        """
        return ''.join([w if ord(w) < 128 else ' ' for w in text])

    def remove_hyperlinks(self, text):
        """
        return text after removing hyperlinks
        """
        return ' '.join([w for w in text.split(' ') if not 'http' in w])

    def get_cleaned_text(self, text):
        """
        return cleaned text(string) for provided tweet text(string)
        """
        cleaned_text = text.replace('\"', '').replace('\'', '').replace('-', ' ')

        cleaned_text = self.remove_non_ascii_chars(cleaned_text)

        # retweet
        if re.match(r'RT @[_A-Za-z0-9]+:', cleaned_text):  # retweet
            if self.remove_retweets: return ''
            retweet_info = cleaned_text[
                           :cleaned_text.index(':') + 2]  # 'RT @name: ' will be again added in the text after cleaning
            cleaned_text = cleaned_text[cleaned_text.index(':') + 2:]
        else:
            retweet_info = ''

        cleaned_text = self.remove_hyperlinks(cleaned_text)

        cleaned_text = cleaned_text.replace('#', 'HASHTAGSYMBOL').replace('@',
                                                                          'ATSYMBOL')  # to avoid being removed while removing punctuations

        tokens = [w.translate(self.punc_table) for w in word_tokenize(cleaned_text)]  # remove punctuations and tokenize
        tokens = [w for w in tokens if
                  not w.lower() in self.stop_words and len(w) > 1]  # remove stopwords and single length words
        cleaned_text = ' '.join(tokens)

        cleaned_text = cleaned_text.replace('HASHTAGSYMBOL', '#').replace('ATSYMBOL', '@')
        cleaned_text = retweet_info + cleaned_text

        return cleaned_text