from . import *
CONFIG = './config.yaml'



class eventDetectionAlgorithms:
    '''
        TODO: documentation + check why yaml is updated yet empty
    '''

    __algorithms = {}

    def __init__(self):
        self.__algorithms = self.get_config_yaml()
        if not self.__algorithms:
            self.__algorithms = {}

    # TODO add algorithms.config file which saves new algorithm
    def add_algorithm(self, algorithm_name, algorithm):
        self.__algorithms[algorithm_name] = algorithm
        self.update_config_yaml()

    def get_algorithms(self):
        return self.__algorithms

    def update_config_yaml(self):
        with open(CONFIG, 'w') as config_file:
            yaml.dump(self.__algorithms, config_file)

    def delete_from_yaml(self, algorithm_name):
        self.__algorithms.pop(algorithm_name)
        self.update_config_yaml()

    def get_config_yaml(self):
        with open(CONFIG, 'r') as config_file:
            return yaml.load(config_file, Loader=yaml.Loader)
