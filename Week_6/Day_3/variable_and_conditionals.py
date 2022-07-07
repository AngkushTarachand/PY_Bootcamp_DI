print('Variable and Conditionals')
#
# name = 'laurent'
# print(name)
#
# print("My name is " + name + " and I am currently doing my 1st Hackathon.")
# print("My name is {} and I am currently doing my 1st Hackathon".format(name))
# print(f"My name is {name} and I am currently doing my 1st Hackathon.")
#
# age = 34
#
# # String formatting and variable display
# print("My name os " + name + " and my age is " + str(age))
# print("My name is {} and my age is {}".format(name, age))
# print(f"My name is {name} and my age is {age}")
#
# print("My name is", name, "and my age is", age)
#
# # Increment a value
# num = 0
# print(num)
#
# num = num + 1
# print(num)
#
# num += 1
# print(num)
#
# # Take User Input
# name = input('Please state your name')
#
# print("My name is " + name)
#
# name = input('Please stage your name: ')
# age = input('Please enter your age: ')
#
# new_age = int(age) + 5
#
# print("My name is " + name + " and my age is " + str(new_age))
# print(f"My age is {name} and my age in 5 years will be {new_age}")
#
# # Conditionals
# # if condition : condition evaluating whether it is True or False
# #     code     : important to be indented for multiple lines
# #                 , will run of condition is true
#
# if int(age) > 18:
#     print(" You are an adult")
# print("Congratulations") # This line will be expressed irrespective of the if statement (not indented)
#
# # if-else statement and elif( equivalent of else if)
# if int(age) > 60:
#     print("You can travel for free in Mauritius")
# elif int(age) == 60:
#     print("Congratulations on being able to travel for free now in Mauritius")
# elif int(age) == 59:
#     print("Next year you will be able to travel for free in Mauritius")
# else:
#     print("Sorry you need to pay to travel")
#
# print('Finished')
#
# # Multiple comparisons
# a = 1
# b = 2
# c = 0
#
# if(a < b) and not (c > a):  # and : both conditions need to be True, not; opposition of boolean value()
#     print('Both conditions are met')
# elif a < b or c > a:  # or :  if at least one condition is true
#     print("At least one condition is met")
# else:
#     print("Conditions not met")
#
# # In
# vowels = "aeiouy"  # string is a sequence of characters
# letter = 'a'
# print(letter in vowels)
# print('b' in vowels)
# print('c' in vowels)
# print('d' in vowels)
# print('e' in vowels)
#
# hobbies = ["TV", "eating", "coding", "gaming"]
# student_hobby = "coding"
# if student_hobby in hobbies:
#     print("Welcome to the Club!")
#


# Sequences - category of data type (List, Tuple, String)

# Lists - versatile sequence type (can contain integers, strings, booleans or more list)
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
print(vowel_list)

vowels_list = [1, 2, 3, 4, 5]
print(vowel_list)

# Tuple - Like a List, BUT they are immutable (they cannot be changed)
vowel_tuple = ('a', 'e', 'i', 'o', 'u', 'y')
print(vowel_tuple)

vowel_tuple = (1, 2)
print(vowel_tuple)

# Strings - special sequence that can only contain characters
vowel_str = "aeiouy"
print(vowel_str)

# indexing in sequence
# starts with zero
print(vowel_list[0])
print(vowel_str[0])
print(vowel_str[0])

# Last element
print(vowel_list[len(vowel_list)-1])
print(vowels_list[-1])
print(vowel_tuple[-1])
print(vowel_str[-1])

# range of elements
print(vowels_list[0:3])  # start: end (but does not include value at end index)
print(vowels_list[:3])
print(vowel_tuple[0:3])
print(vowel_str[0:3])

print(vowels_list[3:])  # if end index not specified, default last index
print(vowel_tuple[3:1])
print(vowel_str[3:])

# Methods
# Update element

vowels_list[0] = 'b'
print(vowels_list)

# vowels_list[10] = 'z' # this will result in indexError - that index does not exist
# print(vowels_list)

# Add a new element
vowels_list.append('z')
print(vowels_list)

# Remove an Element
# vowels_list.remove('a')
vowels_list.remove('z')
print(vowels_list)

# Adding two list
missing_vowel = ['a']
complete_vowels = missing_vowel + vowels_list  # Combining Lists
print(complete_vowels)

# sorting
unsorted_list = ['b', 'm', 'e', 's', 'a']
print(sorted(unsorted_list))

unsorted_nums = [2, 1, -3, 8, -10]
print(unsorted_nums)

# length
print(len(unsorted_nums))

# sum
print(sum(unsorted_nums))

print("Average of unsorted_nums", sum(unsorted_nums)/len(unsorted_nums))
