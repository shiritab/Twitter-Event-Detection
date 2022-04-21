import json
import os

from flask import jsonify
from EventSegmentClusterer import get_events, get_seg_similarity
from TimeWindow import TimeWindow
from TwitterEventDetector import TwitterEventDetector
from Backend.algorithms.eventDetectionAlgorithm import DetectionAlgorithm
class SedTwik(DetectionAlgorithm):


    def __init__(self):
        super().__init__()

    def run_algorithm(self, *data):
        # Parameters
        original_tweet_dir = '../data/original_tweets/' # end with '/'
        clean_tweet_dir = '../data/cleaned_tweets/without_retweets/' # end with '/'
        subwindow_dir = '../data/cleaned_tweets/without_retweets/'  # each file is a subwindow in this folder
        event_output_dir = '../results/last_res'
        wiki_titles_file = '../data/enwiki-titles-unstemmed.txt'
        seg_prob_file = '../data/seg_prob_2012_Oct_11-22.json'
        wiki_Qs_file = '../data/WikiQsEng_non_zero_processed.json'

        to_ret_events=[]
        remove_retweets = True
        max_segment_length = 7
        hashtag_wt = 3
        entities_only = False # False --> use #tag and @name only for event detection
        default_seg_prob = 0.0000001 # for unknown segments
        use_retweet_count = True
        use_followers_count = True
        n_neighbors = 4
        threshold = 4 # for news_worthiness

        ted = TwitterEventDetector(wiki_titles_file, seg_prob_file, wiki_Qs_file, remove_retweets, max_segment_length,
                                   hashtag_wt, use_retweet_count, use_followers_count, default_seg_prob, entities_only)

        # Tweet Cleaning
        #ted.clean_tweets_in_directory(original_tweet_dir, clean_tweet_dir)

        # Segment tweets and create TimeWindow
        print('\nReading SubWindows')
        subwindow_files = [f.name for f in os.scandir(subwindow_dir) if f.is_file()]

        subwindows = []
        for subwindow_name in subwindow_files[:4]: # read timewindow consisting 6 subwindows of 1 hour each
            print('SubWindow:',subwindow_name)
            sw = ted.read_subwindow(subwindow_dir + subwindow_name)
            subwindows.append(sw)
        print('Done\n')
        tw = TimeWindow(subwindows)
        print(tw)

        #next_subwindow = ted.read_subwindow(subwindow_dir + subwindow_files[7])
        #tw.advance_window(next_subwindow)
        #print(tw)

        # Bursty Segment Extraction
        print()
        bursty_segment_weights, segment_newsworthiness = ted.bse.get_bursty_segments(tw)
        seg_sim = get_seg_similarity(bursty_segment_weights, tw)

        # Clustering Bursty Segments
        events = get_events(bursty_segment_weights, segment_newsworthiness, seg_sim, n_neighbors)

        # dump event clusters along with tweets[cleaned ones :-( ] associated with the segments in the cluster
        print('\nEvents will be saved in', event_output_dir)
        if not os.path.exists(event_output_dir):
            os.makedirs(event_output_dir)
        event_no = 0
        for e, event_worthiness in events:
            summarization_list = []
            tweets_ids = []
            dirty_tweets=[]


            tmp_dict = {}
            event_no += 1
            print('\nEVENT:', event_no, 'News Worthiness:', event_worthiness)
            f = open(event_output_dir + str(event_no) + '.txt', 'w', encoding="utf-8")
            f.write(str(e)+' '+str(event_worthiness)+'\n\n')
            for seg_name in e:
                print(seg_name)
                f.write('SEGMENT:' + seg_name + '\n')
                for tweet_id, text ,dirty in set(tw.get_tweets_containing_segment(seg_name)):
                    f.write(f'{tweet_id} {text}, {dirty}\n')
                    summarization_list.append(text)
                    tweets_ids.append(tweet_id)
                    dirty_tweets.append(dirty)
                f.write('-----------------------------------------------------------\n')
                tmp_dict["event"]=e
                tmp_dict["tweets"]=tweets_ids
                tmp_dict["dirty_text"]=dirty_tweets
            to_ret_events.append(tmp_dict)
            f.close()
        with open('hours1-6_res.json', 'w') as f:
            json.dump(to_ret_events, f)
        return to_ret_events