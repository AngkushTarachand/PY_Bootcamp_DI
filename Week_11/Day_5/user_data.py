import json


def add_user():
    user_name = input("Enter Name ")
    user_email = input("Enter email ")
    user_password = input("Enter password ")
    user_dict = {
        "Name": user_name,
        "Email": user_email,
        "Password": user_password
    }
    try:
        f = open("users.json", "a+")
        json_object = json.dumps(user_dict)
        f.write(json_object)
    finally:
        f.close()


def check_user(user):
    if user in open("users.json", "r"):
        return "homepage"
    else:
        return "stay_in"



add_user()
add_user()


