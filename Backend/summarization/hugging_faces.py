from transformers import pipeline
import tensorflow

class HuggingFaces:
	def __init__(self):
		self.summarizer = pipeline("summarization")

	def summarize(self,tweets_list):
		if type(tweets_list) == list:
			text=','.join(tweets_list)[:512]
			return self.summarizer(text, max_length=9, min_length=3, do_sample=False)[0]["summary_text"]
		return tweets_list