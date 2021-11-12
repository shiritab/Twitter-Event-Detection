from flask import Blueprint, jsonify

events = Blueprint("events", __name__)


# @events.route("/")
@events.route("/summary")
def get_summary():
    events_obj = {'events':{
        'event_name':'Bibi lose elections',
        'event_description':'during the last elections Benjanim Netanyahu lost to Naftalie Bennet',
        'date':'2021-11-11',
    }}
    return jsonify(events_obj)


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