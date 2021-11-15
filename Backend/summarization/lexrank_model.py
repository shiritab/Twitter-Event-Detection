from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS
from nltk.corpus import wordnet
from path import Path

class summarization:
    lxr = None
    tweets_dir = None
    docs = []

    def __init__(self, tweets_dir):
        ''' summarization constructor,
        @param tweets_dir: String, A directory path for .txt files '''
        self.tweets_dir = Path(tweets_dir)

    def find_docs(self):
        '''This function saves all documents from .txt files in tweets_dir (in our case docs = tweets)'''
        for file_path in self.tweets_dir.files('*.txt'):
            with file_path.open(mode='rt', encoding='utf-8') as fp:
                self.docs.append(fp.readlines())

    def train_lexrank(self):
        '''LexRank model trains itself over a given list of strings - docs'''
        lxr = LexRank(self.docs, stopwords=STOPWORDS['en'])

    def summarize(self, segments_file):
        '''
        @param segments_dir: String, A .txt file containing all tweets segments
        return values:
            summary - a list with one value, summary with classical lexrank algorithm
            summary_cont - a list with one value, summary with continous lexrank'''
        with open(segments_file, 'r') as f:
            newList = []
            tweetsList = f.readlines()
            for line in tweetsList:
                newLine = ""
                for word in (line.rstrip()).split(" "):
                    if wordnet.synsets(word):
                        newLine += " "+word
                newList.append(newLine)
        sentences = newList

        # get summary with classical LexRank algorithm
        summary = self.lxr.get_summary(sentences, summary_size=1, threshold=.1)
        print(summary)

        # get summary with continuous LexRank
        summary_cont = self.lxr.get_summary(sentences, threshold=None)
        print(summary_cont)

        # get LexRank scores for sentences
        # 'fast_power_method' speeds up the calculation, but requires more RAM
        scores_cont = self.lxr.rank_sentences(
            sentences,
            threshold=None,
            fast_power_method=False,
        )
        print(scores_cont)
        return summary, summary_cont