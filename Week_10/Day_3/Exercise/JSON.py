import json

# my_family = {
#     "parents": ["beth", "Jeery"],
#     "children": ["summer", "Marty"]
# }
#
# with open("names.json", "w+") as f:
#     json.dump(my_family, f, indent=2, sort_keys=True)

# with open("names.json") as f:
#     my_family = json.load(f)
#     print(my_family)
#     print(my_family["children"])

my_family = {
    "parents": ["beth", "Jeery"],
    "children": ["summer", "Marty"]
}

my_family_as_str = json.dumps(my_family)  # from dict to json
print(my_family_as_str)

my_family_as_dict = json.loads(my_family_as_str)  # from string of json to dict

