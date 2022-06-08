# Twitter-Event-Detection

Our website aims to provide a solution for data scientists that work in the area of twitter even detection. This site will alow them to compare between different algorithms and to observe the visualizations result of the clusters between 
algorithms that run over the same datasets.

## Table of Contents
1. [Sidebar](#sidebar)
2. [Trending Page](#trending-page)
3. [Compare Page](#compare-page)
4. [Events By Date Page](#events-by-date-page)
5. [Help Page](#help-page)
6. [About Page](#about-page)
7. [Login Page](#login-page)
__________

## Sidebar
You can go by our different pages by clicking of each of the buttons of the sidebar on the left. ![sidebar](/Frontend/assets/sidebar.png)
__________

## Trending Page
This page contains the following functionalities: 
  ![trending btn](/Frontend/assets/TrendingPage/trendingButton.png)

- Upload a dataset of your own:
  - Click on 'Upload Data' button 
    ![upload btn](/Frontend/assets/TrendingPage/uploadData.png)
    - **what file should user upload? (csv, json, tsv etc.)**

  - Now you can choose the file in 'Data Set' dropdown 
    ![dataset dd](/Frontend/assets/TrendingPage/chooseDataSet.png)

- Run different algorithms:
  - Click on 'Algorithm' dropdown 
    ![algorithm dd](/Frontend/assets/TrendingPage/selectAlgorithm.png)
    - You can choose to only one of the algorithms - SedTwik, Twembeddings or Bert.
  - Click on 'Run' button 
    ![dataset dd](/Frontend/assets/TrendingPage/runAlgorithm.png)
  - Now results will be presented on the graphs below.
__________
## Compare Page
![compare btn](/Frontend/assets/ComparePage/compareButton.png)
This page shows the perfomance difference of the algorithms' you chose.
- **ADD GRAPHS PHOTO**
  - The left graph shows the measurments - **what measurements?**
  - The right graph shows number of tweets/events each algorithm chosen contains.

- Choose what algorithms you wish to compare by picking their checkbox.
  ![algorithms checkbox](/Frontend/assets/ComparePage/algorithmCheckbox.png)

  ![algorithms checkbox](/Frontend/assets/ComparePage/checkAlgorithm.png)
__________

## Events By Date Page
![events btn](/Frontend/assets/EventsPage/eventsButton.png)
Here you need to pick a date in the date picker 
![datepicker](/Frontend/assets/EventsPage/datepicker.png)

after you chose a date you will see all events occured on that date, clicking on each of them will forward you to the event's page.
![event click](/Frontend/assets/EventsPage/clickEvent.png)

### Event's page
- We present here 2 informative graphs, 
  ![dataset dd](/Frontend/assets/EventPage/eventPageGraphs.png)
  - The left one shows event's sentiment analysis over time
  - The right one shows tweets amount distribution over time.

 - At the bottom we present each event's tweet.
  ![dataset dd](/Frontend/assets/EventPage/eventPageTweets.png)
__________
## Help Page
![help btn](/Frontend/assets/helpButton.png)
This page contains README.md file.
__________
## About Page
![about btn](/Frontend/assets/aboutButton.png)
This page contains some information about us, whom created this site.
__________
## Login Page
![login btn](/Frontend/assets/LoginPage/loginButton.png)
In order to have some unique functionalities - Upload data, **use twitter api?** - you have to be registered to our website. 

If you haven't registered yet - Now is the time and you can do it by clicking on this link 
![register link](/Frontend/assets/LoginPage/registerLink.png)

