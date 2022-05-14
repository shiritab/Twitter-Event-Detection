


class eventDetectionAlgorithms:
    __algorithms = {
        "sedtwik": None,
        "twembeddings": None
    }

    def add_algorithm(self, algorithm_name, algorithm):
        self.__algorithms[algorithm_name] = algorithm

    def get_algorithms(self):
        return self.__algorithms