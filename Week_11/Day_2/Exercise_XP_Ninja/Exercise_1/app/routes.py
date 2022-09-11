import flask
from faker import Faker
from app import flask_app


@flask_app.route("/CV")
def index():
    fake = Faker("it_IT")
    faker_list = []
    for _ in range(10):
        faker_list.append(fake.name())

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

    return flask.render_template("CV.html", username=faker_list,
                                 user_hobbies=my_hobbies,
                                 user_skill=my_skills,
                                 user_strength=my_strength,
                                 user_weakness=my_weakness,

                                 )
