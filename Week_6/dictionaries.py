print('Dictionaries')

# Defining a dictionary
# key-value pair (Key: value)
# value can be in ANY data type
# Keys need to be unique. No duplicate
# Unordered till python 3.6
# Ordered as from Python 3.7

students_dict = {
    "student1": "Joeri",
    "student2": "Ally",
    "student3": "Shivastav",
    "student4": "Kadeer",
    "student5": "Laurent",
    "student6": "Angkush",
    "student7": "Bruno",
    "ages": [25, 24, 24, 23, 34, 19, 50]
}

print(students_dict)

# Access the data - using key
print(students_dict['student1'])
print("This first student is {}".format(students_dict['student1']))

# Access the data - using index
# keys
keys_student = list(students_dict)
print(keys_student[0])
print(students_dict[keys_student[0]])

# values
values_students = list(students_dict.values())
print(values_students[0])

sample_dict = {
   "class": {
      "student": {
         "name": "Mike",
         "marks": {
            "physics": 70,
            "history": 80
         }
      }
   }
}

history = sample_dict
print(history)

history = sample_dict['class']['student']['marks']['history']

# Update dictionary

students_dict['students6'] = "Tooshar"
print(students_dict)

# Add new entry
students_dict['Instructor'] = 'Damien'
print(students_dict)

# Delete / Remove an entry
del students_dict['student4']
print(students_dict)



# Loop through dictionary.
for student in students_dict:
    if students_dict[student] == 'Bruno':
        print('student4 is present')
        break
    else:
        print(student, students_dict[student])

# Get dictionary of keys, values and items
print(students_dict.keys())
print(students_dict.values())
print(students_dict.items())

# Merge dictionaries
new_instructor = {'New instructor': Nirmal}
students_dict.update(new_instructor)

# Using items in for Loop

for key, value in students_dict.items():
    print("{} is {}".format(key, val))

#Exercise

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

keys_to_remove = {}