import torch

torch.cuda.is_available()
import pandas as pd
import pickle
import random
from tqdm.notebook import tqdm

from sklearn.feature_extraction.text import CountVectorizer
from umap import UMAP
from bertopic import BERTopic
import gensim.corpora as corpora
from gensim.models.coherencemodel import CoherenceModel
from itertools import product
from tqdm import tqdm_notebook as tqdm