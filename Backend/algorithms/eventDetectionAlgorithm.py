
'''
this interface is the basic blueprint API all event detection algorithms need to implement
in order to be compatible with the systems front end.

'''

class DetectionAlgorithm:


    def __init__(self):
        self.eventResutls = None

    def run_algorithm(self, *data):
        '''
        applies algorithm's method on given data
        :param data:
        :return: JSON file with results
        '''
        pass

    def upload_data(self, data):
        pass

    def get_results(self, *args):
        '''
        each algorithm ahs a different eay of getting and returning its results.
        this method is where its is implemanted
        :return:
        JSON file with relevant results
        '''
        pass

    def get_results_by_date(self,date):
        pass

    def summarize(self):
        pass

