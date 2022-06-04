# 1. Algorithm Addition

In order to add a new algorithm to our backend, do the following stpes:

1. Create a new package under Backend/algorithms/<algorithm_name>
   1. Open a new <algorithm_name>.py file (ex. bert_topic.py)

2. Import the followings within the python file

    ```
    import json
    import os
    import sys
    from ..eventDetectionAlgorithm import DetectionAlgorithm
    ```
3. Create a class which inehrits from DetectionAlgorithm

    ```
    Class <algorithm_class_name>(DetectionAlgorithm):

        def __init__(self):
            self.results_path = "../results/<algorithm_name>/"
            self.eventResults = ""
            self.data = ""

        # body of class
    ```
    ex. results_path = "../results/bert_topic/"
4. Implement run_algorithm(self, data) method

    This method runs the algorithm implementation with the given dataset which was picked in the UI, and returns nothing.

    The datasets stored in this system of the following structure:
    ```
    .json file containing a list of tweet objects like the structure below: 

    {
        "tweet_id": "123",
        "date": 1349939974000, 
        "text": "sample text", "retweet_count": 1, "favorite_count": 0, 
        "created_at": "Thu Oct 11 07:19:34 +0000 2012", 
        "user": {
            "id": "1", 
            "name": "bigbookworm", "author_full_name": "Christian Kohnle", 
            "statuses_count": 8854, "followers_count": 1739, "friends_count": 2101, "favourites_count": 0
            }, 
        "entities": {
            "hashtags": [], "user_mentions": []
            }
    }
    ```
        

    ```
    def run_algorithm(self, data):
        # algorithm implementation
    ```
    The expected results json file structure,
    ```
    [
        {
            "event":"Event title example",
            "tweets": [
                1,
                2,
                3
            ],
            "dirty_text": [
                "Tweet text 1", 
                "Tweet text 2", 
                "Tweet text 3"
            ],
            "dates": [
                "2022-05-06", 
                "2022-05-06", 
                "2022-04-08"
            ],
            "dates_set": [
                "2022-05-06", 
                "2022-04-08"
            ]
        }
    ]
    ```
    ***Notice***: 
    1. Please save results to ```self.eventResutls``` 
    2. In order to save runtime for the next time you can:
        1. Save results to a file with ```self.save_results(data)```
        2. Get saved results with ```self.get_results(data)``` 
        
5. Now, after you've done the last 4 steps you can add the algorithm to our UI. run the following 2 lines, ***Notice*** once you've done it there's no reason executing it again.

    ```
    from Backend.routing.endpoints.algorithm import algorithms_object

    algorithms_object.add_algorithm("<algorithm_name>",<algorithm_class_name>())

    # example, algorithms_object.add_algorithm("Bert",Bert())
    ```
6. ***In case you wish to delete it from the UI for some reasons***, please execute the following lines.
   
   ```
   from Backend.routing.endpoints.algorithm import algorithms_object

    algorithms_object.delete_from_yaml("<algorithm_name>")

    # example, algorithms_object.delete_from_yaml("Bert")
   ```

   ***Notice:*** algorithm's name must be the ***exact*** same name as added. (It's the same name as seen on the UI)

7. Create algorithm's results directory under Backend/results/<algorithm_name> (ex. Backend/results/bert_topic)

## 1.1. That's it! now you can use it on our web page. Good luck ☺
