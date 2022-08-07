import json

json_file = open("file.json")
family = json.load(json_file)
print(family)

Jane_children = family["children"]
print(Jane_children)

Jane_children[0]["favourite_color"] = "blue"
Jane_children[1]["favourite_color"] = "blue"
print(Jane_children)

with open('file.json', 'w') as f:
    json.dump(family, f, indent=2, sort_keys=True)
