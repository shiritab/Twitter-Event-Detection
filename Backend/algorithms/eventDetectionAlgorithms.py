from . import *
CONFIG = './config.yaml'



class eventDetectionAlgorithms:

    __algorithms = {}

    def __init__(self):
        '''
        Withdraws all algorithms from config.yaml file
        '''
        self.__algorithms = self.get_config_yaml()
        if not self.__algorithms:
            self.__algorithms = {}

    def add_algorithm(self, algorithm_name, algorithm):
        '''
        Given algorithm name and an algorithm object, 
        creates new algorithm in algorithms dict and updates config.yaml file.
        :param algorithm_name - string
        :param algorithm - DetectionAlgorithm
        '''
        self.__algorithms[algorithm_name] = algorithm
        self.update_config_yaml()

    def get_algorithms(self):
        '''
        Returns algorithms dict
        '''
        return self.__algorithms

    def update_config_yaml(self):
        '''
        Updates config.yaml file with current algorithms dict
        '''
        with open(CONFIG, 'w') as config_file:
            yaml.dump(self.__algorithms, config_file)

    def delete_from_yaml(self, algorithm_name):
        '''
        Given algorithm name,
        deletes it's (key, value) pair from algorithms dict and update config.yaml file
        '''
        self.__algorithms.pop(algorithm_name)
        self.update_config_yaml()

    def get_config_yaml(self):
        '''
        Returns algorithms dict in config.yaml
        '''
        with open(CONFIG, 'r') as config_file:
            return yaml.load(config_file, Loader=yaml.Loader)
