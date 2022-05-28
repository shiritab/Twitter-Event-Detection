import json
import pandas as pd
import logging
import yaml
import argparse
import csv
from transformers import pipeline
import tensorflow
# from sklearn.cluster import DBSCAN
from Backend.algorithms.twembed.twembeddings.build_features_matrix import build_matrix
from Backend.algorithms.twembed.twembeddings.clustering_algo import ClusteringAlgoSparse, ClusteringAlgo
from Backend.algorithms.twembed.twembeddings.eval import general_statistics, cluster_event_match, mcminn_eval

logging.basicConfig(format='%(asctime)s - %(levelname)s : %(message)s', level=logging.INFO)
text_embeddings = ['tfidf_dataset', 'tfidf_all_tweets', 'w2v_gnews_en', "elmo", "bert", "sbert_nli_sts", "use"]
parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('--model',
                    nargs='+',
                    required=True,
                    choices=text_embeddings,
                    help="""
                    One or several text embeddings
                    """
                    )
parser.add_argument('--dataset',
                    required=True,
                    help="""
                    Path to the dataset
                    """
                    )

parser.add_argument('--lang',
                    required=True,
                    choices=["en", "fr"])

parser.add_argument('--annotation',
                    required=False,
                    choices=["examined", "annotated", "no"])

parser.add_argument('--threshold',
                    nargs='+',
                    required=False
                    )

parser.add_argument('--batch_size',
                    required=False,
                    type=int
                    )

parser.add_argument('--remove_mentions',
                    choices=[0, 1],
                    default=None,
                    type=int,
                    required=False
                    )

parser.add_argument('--window',
                    required=False,
                    default=24,
                    type=int
                    )

def main(args):
    print(args)
    with open("../algorithms/twembed/options.yaml", "r") as f:
    # with open("/Backend/utils_backend/twembeddings/options.yaml", "r") as f:
        options = yaml.safe_load(f)
    for model in args["model"]:
        # load standard parameters
        params = options["standard"]
        logging.info("Clustering with {} model".format(model))
        if model in options:
            # change standard parameters for this specific model
            for opt in options[model]:
                params[opt] = options[model][opt]
        for arg in args:
            if args[arg] is not None:
                # params from command line overwrite options.yaml file
                if arg == "remove_mentions":
                    params[arg] = bool(args[arg])
                else:
                    params[arg] = args[arg]

        params["model"] = model
        return test_params(**params)


def test_params(**params):
    X, data = build_matrix(**params)
    params["window"] = int(data.groupby("date").size().mean()*params["window"]/24// params["batch_size"] * params["batch_size"])
    logging.info("window size: {}".format(params["window"]))
    params["distance"] = "cosine"
    # params["algo"] = "DBSCAN"
    # params["min_samples"] = 5
    thresholds = params.pop("threshold")
    for t in thresholds:
        logging.info("threshold: {}".format(t))
        # clustering = DBSCAN(eps=t, metric=params["distance"], min_samples=params["min_samples"]).fit(X)
        if params["model"].startswith("tfidf") and params["distance"] == "cosine":
            clustering = ClusteringAlgoSparse(threshold=float(t), window_size=params["window"],
                                              batch_size=params["batch_size"], intel_mkl=False)
        else:
            clustering = ClusteringAlgo(threshold=float(t), window_size=params["window"],
                                        batch_size=params["batch_size"],
                                        distance=params["distance"])
        clustering.add_vectors(X)
        y_pred = clustering.incremental_clustering()
        # y_pred = clustering.labels_
        stats = general_statistics(y_pred)
        p, r, f1 = cluster_event_match(data, y_pred)
        data["pred"] = data["pred"].astype(int)
        candidate_columns = ["date", "time", "label", "pred", "user_id_str", "id","text"]
        result_columns = []
        for rc in candidate_columns:
            if rc in data.columns:
                result_columns.append(rc)
        data[result_columns].to_csv(params["dataset"].replace(".", "_results."),
                                    index=False,
                                    sep="\t",
                                    # quoting=csv.QUOTE_NONE
                                    )
        try:
            mcp, mcr, mcf1 = mcminn_eval(data, y_pred)
        except ZeroDivisionError as error:
            logging.error(error)
            continue
        stats.update({"t": t, "p": p, "r": r, "f1": f1, "mcp": mcp, "mcr": mcr, "mcf1": mcf1})
        stats.update(params)
        stats = pd.DataFrame(stats, index=[0])
        logging.info(stats[["t", "model", "tfidf_weights", "p", "r", "f1"]].iloc[0])
        if params["save_results"]:
            try:
                results = pd.read_csv("results_clustering.csv")
            except FileNotFoundError:
                results = pd.DataFrame()
            stats = results.append(stats, ignore_index=True)
            stats.to_csv("results_clustering.csv", index=False)
            logging.info("Saved results to results_clustering.csv")
    return build_dictionary(data)

def build_dictionary(data):
    sortedData = data.sort_values(["pred"],axis = 0)

    labels = set(data["pred"].values)

    groups = data.groupby(["pred"])
    events = sorted([g for i,g in groups],key =  lambda x : x.size, reverse=True)
    events = events[:100] if len(events) >2 else events
    summarizer = None
    return_JSON = []
    for event in events:
        # fullText = ""
        eventDict = {"event":None, "tweets": [], "dirty_text": [], "dates":[]}
        for i,tweet in event.iterrows():
            # print(tweet)
            eventDict["tweets"].append(str(tweet["id"]))
            eventDict["dirty_text"].append(tweet["text"])
            eventDict["dates"].append(tweet["date"][:4]+"-"+tweet["date"][4:6]+"-"+tweet["date"][6:])
        dates = set(eventDict["dates"])
        eventDict["dates_set"] = list(dates)
        return_JSON.append(eventDict)

    return return_JSON


def sort_results_by_cluster(path):
    data = pd.read_csv(path,delimiter="\t")
    sortedData = data.sort_values(["pred"],axis = 0)
    labels = set(data["pred"].values)
    groups = data.groupby(["pred"])
    print(groups)
    events = sorted([g for i,g in groups],key =  lambda x : x.size, reverse=True)
    events = events[:2] if len(events) >2 else events
    print ("here")
    summarizer = None
    return_JSON = []
    for event in events:
        # fullText = ""
        eventDict = {"event":None, "tweets": [], "dirty_text": []}
        for i,tweet in event.iterrows():
            # print(tweet)
            eventDict["tweets"].append(str(tweet["id"]))
            eventDict["dirty_text"].append(tweet["text"])
        # eventDict["event"]= event["pred"][0]
        return_JSON.append(eventDict)
        # print (fullText)
        # print("$$$$$$")
    with open('../../utils_backend/2012-10-12_french.json', 'r+') as f:
        data = json.load(f)
        data += ([e for e in return_JSON])
        json.dump(return_JSON, f)


def summarize(text, summarizer):
    # print(summarizer(text, max_length=9, min_length=3, do_sample=False))
    return text


# if __name__ == '__main__':
#     # summarizer = pipeline("summarization")
#     # summerize("text",summarizer)
#
#     main({'model': ['tfidf_all_tweets'],
#           'dataset': f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only.tsv',
#           'lang': 'en',
#           'annotation': 'no',
#           'threshold': ['0.7'],
#           'batch_size': None,
#           'remove_mentions': None,
#           'window': 24})
#
#     sort_results_by_cluster(f'C:\\Users\\user\\Desktop\\tagged tweets\\event2012_labeled_only_2_results.tsv')

    # args = vars(parser.parse_args())
    # main(args)