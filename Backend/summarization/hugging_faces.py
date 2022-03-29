from transformers import pipeline
import tensorflow

class HuggingFaces:
	'''
	this class uses a summarizer to summarize set of strings.
	'''
	def __init__(self):
		self.summarizer = pipeline("summarization")

	def summarize(self,tweets_list):
		'''
		given a tweets list we join them all by a comma and we send it to the summarizer we have created before, the summary returned is the event.
		@param tweets_list: string[]
		return string
		'''
		if type(tweets_list) == list:
			text=','.join(tweets_list)[:512]
			return self.summarizer(text, max_length=9, min_length=3, do_sample=False)[0]["summary_text"]
		return tweets_list
