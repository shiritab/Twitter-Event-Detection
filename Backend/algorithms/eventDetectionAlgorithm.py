import json
import os
import sys

from ..summarization import hugging_faces
from ..utils_backend.emotion_tweet import EmotionTweet

'''
this interface is the basic blueprint API all event detection algorithms need to implement
in order to be compatible with the systems front end.

'''

class DetectionAlgorithm:


    def __init__(self):
        self.eventResutls = None
        self.results_path = None

    def run_algorithm(self, *data):
        '''
        applies algorithm's method on given data
        :param data:
        :return: JSON file with results
        '''
        pass

    def upload_data(self, data):
        pass

    def get_results(self, data):
        '''
        Checks if a results file already exists in the algorithm's results dir.
        If so then returns the results object - otherwise returns None
        :return:
        JSON file with relevant results
        '''

        self.data = data
        if os.path.isfile(self.results_path + "results_{}".format(self.data)):
            with open(self.results_path + "results_{}".format(self.data), "r") as results_file:
                self.eventResutls = json.load(results_file)
                return self.eventResutls

        return None

    def save_results(self, data):
        '''
        This methods saves the data object into a file under algorithm's results dir.
        :param data: dict
        :return: void
        '''

        with open(self.results_path + "results_{}".format(data), "w") as file_results:
            json.dump(self.eventResutls, file_results)


    def get_results_by_date(self,date):
        # TODO: check if works
        events = []
        if self.eventResults:
            for event_obj in self.eventResults:
                if date in event_obj.dates_set:
                    events.append(event_obj)
        return events

    def summarize(self):
        if os.path.isfile(self.results_path + "summarized_{}".format(self.data)):
            with open (self.results_path + "summarized_{}".format(self.data), "r") as summarized_file:
                return json.load(summarized_file)

        data=self.eventResutls
        hg = hugging_faces.HuggingFaces()
        for i in range(len(data)):
            # summarize for event name
            dictionary = data[i]
            summary = hg.summarize(dictionary["dirty_text"])
            # calc tweet emotion
            if "tweets_emotion" not in dictionary:
                dictionary["tweets_emotion"] = EmotionTweet().find_emotion(dictionary["dirty_text"])
            dictionary['event'] = summary
            data[i] = dictionary
            sys.stdout.write('\r' + "summarizing processing: {}/{}".format(i,len(data)))
            sys.stdout.flush()
        with open(self.results_path + "summarized_{}".format(self.data), 'w') as summarized_file:
            json.dump(data, summarized_file)

        return data

