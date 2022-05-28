import json
import sys

from . import *
from ...summarization import hugging_faces
from ...utils_backend.emotion_tweet import EmotionTweet


class SedTwik(DetectionAlgorithm):


    def __init__(self):
        self.results_path = "../results/sedwik/"
        self.eventResutls = ""
        self.data = ""

    def run_algorithm(self, data):
        results = self.get_results(data)
        if results:
            return results

        # Parameters
        clean_tweet_dir = '../data/cleaned_tweets/without_retweets/'  # end with '/'
        if data == "event2012.json":
            subwindow_dir = '../data/tagged_tweets/'  # each file is a subwindow in this folder
        else:
            # TODO i don't think that's going to work
            subwindow_dir = '../data/uploaded/'

        event_output_dir_text = '../results/sedwik_output_text/'
        event_output_dir_json = '../results/sedwik/'

        wiki_titles_file = '../data/enwiki-titles-unstemmed.txt'
        seg_prob_file = '../data/seg_prob_2012_Oct_11-22.json'
        wiki_Qs_file = '../data/WikiQsEng_non_zero_processed.json'

        subwindows_directories = [f.name for f in os.scandir(subwindow_dir) if f.is_dir()]
        print(subwindows_directories)
        subwindow_files = []
        for dir_name in subwindows_directories:
            subwindow_files += [dir_name + "/" + f.name for f in os.scandir(subwindow_dir + dir_name) if f.is_file()]
        print(subwindow_files)
        subwindows = []

        # summary_model=summarization()
        remove_retweets = True
        max_segment_length = 4
        hashtag_wt = 3
        entities_only = False  # False --> use #tag and @name only for event detection
        default_seg_prob = 0.0000001  # for unknown segments
        use_retweet_count = True
        use_followers_count = True
        n_neighbors = 1
        threshold = 4  # for news_worthiness

        first_index = 0
        while first_index < len(subwindow_files):
            ted = TwitterEventDetector(wiki_titles_file,
                                       seg_prob_file,
                                       wiki_Qs_file,
                                       remove_retweets,
                                       max_segment_length,
                                       hashtag_wt,
                                       use_retweet_count,
                                       use_followers_count,
                                       default_seg_prob,
                                       entities_only)
            print("first inedx is :{}".format(first_index))
            # Tweet Cleaning
            # ted.clean_tweets_in_directory(original_tweet_dir, clean_tweet_dir)

            # Segment tweets and create TimeWindow
            print('\nReading SubWindows')

            # subfolders = [f.path for f in os.scandir(folder) if f.is_dir()]

            to_ret_events = []
            for subwindow_name in subwindow_files[
                                  first_index:first_index + 6]:  # read timewindow consisting 6 subwindows of 1 hour each
                print('SubWindow:', subwindow_name)
                sw = ted.read_subwindow(subwindow_dir + subwindow_name)
                subwindows.append(sw)
            print('Done\n')
            tw = TimeWindow(subwindows)
            print(tw)

            # next_subwindow = ted.read_subwindow(subwindow_dir + subwindow_files[7])
            # tw.advance_window(next_subwindow)
            # print(tw)

            # Bursty Segment Extraction
            print()
            bursty_segment_weights, segment_newsworthiness = ted.bse.get_bursty_segments(tw)
            seg_sim = get_seg_similarity(bursty_segment_weights, tw)

            # Clustering Bursty Segments
            events = get_events(bursty_segment_weights, segment_newsworthiness, seg_sim, n_neighbors)

            # dump event clusters along with tweets[cleaned ones :-( ] associated with the segments in the cluster
            print('\nEvents will be saved in', event_output_dir_text)
            if not os.path.exists(event_output_dir_text):
                os.makedirs(event_output_dir_text)
            event_no = 0
            for e, event_worthiness in events:
                summarization_list = []
                tweets_ids = []
                dirty_tweets = []

                tmp_dict = {}
                print('\nEVENT:', event_no, 'News Worthiness:', event_worthiness)
                f = open(event_output_dir_text + "tagged_tweets_res1" + '.txt', 'w', encoding="utf-8")

                # f = open(event_output_dir_text +subwindow_files[first_index+event_no][:-5].replace("/","_")+ '.txt', 'w', encoding="utf-8")
                event_no += 1
                f.write(str(e) + ' ' + str(event_worthiness) + '\n\n')
                for seg_name in e:
                    print(seg_name)
                    f.write('SEGMENT:' + seg_name + '\n')
                    for tweet_id, text, dirty in set(tw.get_tweets_containing_segment(seg_name)):
                        f.write(f'{tweet_id} {text}, {dirty}\n')
                        summarization_list.append(text)
                        tweets_ids.append(tweet_id)
                        dirty_tweets.append(dirty)
                    f.write('-----------------------------------------------------------\n')
                    tmp_dict["event"] = e
                    tmp_dict["tweets"] = tweets_ids
                    tmp_dict["dirty_text"] = dirty_tweets
                to_ret_events.append(tmp_dict)
                f.close()
            # with open(event_output_dir_json + "/" + subwindow_files[first_index][:-5].replace("/", "_") + "__" +subwindow_files[first_index + 5].replace("/", "_"), 'w') as f:

            with open(event_output_dir_json + "/" + "results_{}".format(data), 'w') as f:
                json.dump(to_ret_events, f)
            first_index += 6

        # return just the last excute of 6 json files. the others will be saved.
        self.eventResults = to_ret_events
        return to_ret_events
