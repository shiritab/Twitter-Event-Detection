from lexrank import LexRank
from lexrank.mappings.stopwords import STOPWORDS
from nltk.corpus import wordnet
from path import Path

documents = []
documents_dir = Path('C:/Users/שירי/Documents/GitHub/Twitter-Event-Detection/data/tweets')

for file_path in documents_dir.files('*.txt'):
    with file_path.open(mode='rt', encoding='utf-8') as fp:
        documents.append(fp.readlines())

lxr = LexRank(documents, stopwords=STOPWORDS['en'])

with open('C:/Users/שירי/Documents/GitHub/Twitter-Event-Detection/data/events/1.txt', 'r') as f:
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
summary = lxr.get_summary(sentences, summary_size=1, threshold=.1)
print(summary)

# ['Mr Osborne said the coalition government was planning to change the tax '
#  'system "to make it fairer for people on low and middle incomes", and '
#  'undertake "long-term structural reform" of the banking sector, education and '
#  'the welfare state.',
#  'The BBC understands that as chancellor, Mr Osborne, along with the Treasury '
#  'will retain responsibility for overseeing banks and financial regulation.']


# get summary with continuous LexRank
summary_cont = lxr.get_summary(sentences, threshold=None)
print(summary_cont)

# ['The BBC understands that as chancellor, Mr Osborne, along with the Treasury '
#  'will retain responsibility for overseeing banks and financial regulation.']

# get LexRank scores for sentences
# 'fast_power_method' speeds up the calculation, but requires more RAM
scores_cont = lxr.rank_sentences(
    sentences,
    threshold=None,
    fast_power_method=False,
)
print(scores_cont)