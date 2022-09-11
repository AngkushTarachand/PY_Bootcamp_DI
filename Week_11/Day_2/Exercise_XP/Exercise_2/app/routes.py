import flask

from app import flask_app


@flask_app.route("/CV")
def index():
    name = "Tooshar Rohit Tarachand"
    my_hobbies = ["singing", "playing keyboard",
                  "coding", "gardening"]
    my_skills = [
        "Microsoft Office",
        "HTML",
        "CSS",
        "Javascript",
        "Python"
    ]

    my_strength = [
        "versatility",
        "good verbal and written conversion"
    ]

    my_weakness = [
        "Shyness",
        "Procrastination"
    ]

    return flask.render_template("CV.html", username=name,
                                 user_hobbies=my_hobbies,
                                 user_skill=my_skills,
                                 user_strength=my_strength,
                                 user_weakness=my_weakness,

                                 )
