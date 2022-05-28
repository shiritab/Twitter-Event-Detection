# Algorithm Addition

In order to add a new algorithm to our backend, do the following stpes:

1. Create a new package under Backend/algorithms/<algorithm_name>
   1. Open a new <algorithm_name>.py file (ex. bert_topic.py)

2. Import the followings

    ```
    import json
    import os
    import sys
    from ..eventDetectionAlgorithm import DetectionAlgorithm
    ```
3. Create a class which inehrits from DetectionAlgorithm

    ```
    Class <algorithm_class_name>(DetectionAlgorithm):
        algorithm_name = "<algorithm_name>"
        results_path = "../results/<algorithm_name>/"
        data = ""

        # body of class
    ```
    ex. results_path = "../results/bert_topic/"
4. Implement run_algorithm(self, data) method

    ```
    def run_algorithm(self, data):
        self.data = data
        if os.path.isfile(self.results_path + "results_{}".format(self.data)):
            with open(self.results_path + "results_{}".format(self.data), "r") as results_file:
                self.eventResutls = json.load(results_file)
                return

        # algorithm implementation
    ```
   This method runs the algorithm implementation with the given dataset which was picked in the UI, and returns nothing.
   
    ***Notice***: 
    1. Before the algorithm implementation you must copy the first 7 lines, they take the existing results for the same dataset if any at all. 
    2. Afterwards you should save the returned results to
    ```self.eventResutls``` 
    3. Save results to a file with following
        ```
        with open(self.results_path + "results_{}".format(data) , "w") as file_results:
                json.dump(self.eventResutls, file_results)

        ```
5. Implement summarize(self) method as follows,

    ```
    def summarize(self):
        super().summarize()
    ```

6. Now, after you've done the last 4 steps you can add the algorithm to our UI. run the following 2 lines, ***Notice*** once you've done it there's no reason executing it again.

    ```
    from Backend.routing.endpoints.algorithm import algorithms_object

    algorithms_object.add_algorithm("<algorithm_name>",<algorithm_class_name>())

    # example, algorithms_object.add_algorithm("Bert",Bert())
    ```
7. ***In case you wish to delete it from the UI for some reasons***, please execute the following lines.
   
   ```
   from Backend.routing.endpoints.algorithm import algorithms_object

    algorithms_object.delete_from_yaml("<algorithm_name>")

    # example, algorithms_object.delete_from_yaml("Bert")
   ```

   ***Notice:*** algorithm's name must be the ***exact*** same name as added. (It's the same name as seen on the UI)


## That's it! now you can use on our web page. Good luck ☺
