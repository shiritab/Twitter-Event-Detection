import json
from Backend.summarization import hugging_faces
from flask import Blueprint, jsonify
from Backend.utils_backend.emotion_tweet import EmotionTweet
from .algorithm import algorithms_object
# Do not delete this line
events = Blueprint("events", __name__)
####


@events.route("/summary/<algorithm>")
def get_algorithm_summary(algorithm):
    # path = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\\2012-10-12_{}.json".format(algorithm)
    # with open(path, 'r') as file:
    #     data = json.load(file)
    #     if data[0]['summarized'] == "true":
    #         return jsonify(data)
    #     hg = hugging_faces.HuggingFaces()
    #     for i in range(len(data)):
    #         # summarize for event name
    #         dictionary = data[i]
    #         if algorithm == "sedwik":
    #             summary = hg.summarize(dictionary["event"])
    #         elif algorithm == "twembeddings":
    #             summary = hg.summarize(dictionary["dirty_text"])
    #         # calc tweet emotion
    #         if "tweets_emotion" not in dictionary:
    #             dictionary["tweets_emotion"] = EmotionTweet().find_emotion(dictionary["dirty_text"])
    #         dictionary['event'] = summary
    #         data[i] = dictionary
    #
    # with open(path, 'w') as file:
    #     json.dump(data, file)

    return jsonify(algorithms_object.get_algorithms(algorithm).summarize())


@events.route("/events/<algorithm>/<date>")
def get_events_by_date(date, algorithm):
    prefix = r"C:\Users\user\Documents\GitHub\Twitter-Event-Detection\Backend\results\\"
    with open(prefix + "{}_{}.json".format(date, algorithm)) as date_file:
        data = json.load(date_file)
        return jsonify(data)


# below are examples for using post or get AND summary example

# @events.route("/create-post", methods=['GET', 'POST'])
# def create_post():
#     if request.method == "POST":
#         text = request.form.get('text')

#         if not text:
#             flash('Post cannot be empty', category='error')
#         else:
#             post = Post(text=text, author=current_user.id)
#             db.session.add(post)
#             db.session.commit()
#             flash('Post created!', category='success')
#             return redirect(url_for('views.home'))

#     return render_template('create_post.html', user=current_user)

# @events.route("/")
# @events.route("/summary")
# def get_summary():
#     events_obj = {'events':{
#         'event_name':'Bibi lose elections',
#         'event_description':'during the last elections Benjanim Netanyahu lost to Naftalie Bennet',
#         'date':'2021-11-11',
#     }}
#     return jsonify(events_obj)