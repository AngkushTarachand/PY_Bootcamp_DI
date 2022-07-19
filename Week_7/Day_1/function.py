# Defining a function
def name_of_the_function():
    """Docstrings - Provide some information about the function"""
    print("Hello World!")
    print("Happy to see you guys  back!")


# Calling a function
name_of_the_function()

# Passing information to a function


def say_hello(name):
    print("Hello {}".format(name))

#
# say_hello('Laurent')
# say_hello('Angkush')

students = [
    'Joeri',
    'Ally',
    'Laurent',
    'Shivastav',
    'Kadeer',
    'Bruno',
    'Angkush'
]

for student in students:
    say_hello(student)

# Two or more parameters(Try not to use more than 5 parameters


def find_sum(a, b):
    print('{}'.format(a + b))


find_sum(1, 2)
find_sum(2, 3)

# Default values
# find_sum(1)


def find_sum_default(a, b=None):
    if a is None:
        print('Both argument missing')
    elif b is None:
        print('Second argument missing')
    else:
        print('{}'.format(a+b))


# find_sum_default()
find_sum_default(1)
find_sum_default(1, 2)


def say_hello_lang(username, language):
    if language == "EN":
        print("Hello" + username)
    elif language == "FR":
        print("Bonjour" + username)
    else:
        print("This Language is not supported: " + language)


say_hello_lang("Rick", "FR")
say_hello_lang("Bruno", "EN")
say_hello_lang("Francesco", "IT")

# Keywords Arguments (name-value pair)

say_hello_lang("FR", "Rick")
say_hello_lang(language="FR", username="Rick")

# Always specify keyword argument AFTER positional argument
say_hello_lang("Rick", language="FR")

# Global Scope
day = "Monday"


def get_today(temp):
    print("Today is {} and it is {}C".format(day, temp))


get_today(18)

# print(temp) # temp is defined only within the function - local scope


def find_sum_return(a, b):
    print('{}'.format(a + b))
    return a + b


sum = find_sum_return(1, 3)
print("Sum is {}".format(sum))

# Returning more than 1 value


def format_name(first_name, last_name):
    return (first_name.title(), last_name.title())


print(format_name("damien", 'mAlLet'))

first_name, last_name = format_name("damIEN", "mAlLet")
print("Name is {} {}".format(first_name, last_name))


def calculation(a, b):
    sum1 = a + b
    sub1 = a - b
    return sum1, sub1


res = calculation(40, 10)
print(res)

# List as an argument


def greet_persons(persons):
    for person in persons:
        print("Hello {}".format(person.title()))


greet_persons(students)


# Lambda functions
# A squaring lambda function
square1 = lambda n: n*n
num = square1(5)
print(num)

# A subtraction lambda function with multiple
sub = lambda x, y: x-y
print(sub(5, 3))

# Mapping using lambda function
myList = [10, 25, 17, 9, 30, -5]

# Double the value of each element
myList2 = map(lambda n: n*2, myList)
print(myList2)
print(list(myList2))

# Filtering using lambda
myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiple of 5
myList3 = filter(lambda n: n % 5 == 0, myList)
print(myList3)
print(list(myList3))


# Exercise
# Find the standard deviation of a lost of values
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Work out the Mean (the simple average of the numbers)
# def find_mean(nums):
#     return sum(nums)/len(nums)
#
# u = find_mean(values)

# Then for each number: subtract the Mean and square the result.

# var = find_mean(diff)
# Then work out the mean of those squared differences.
# Take the square root of that and we are done!


# def find_mean1(nums):
#     return sum(nums)/len(nums)
#
#
# u = find_mean1(values)
#
# diff = map(lambda n: (n-u)*(n-u), values)
# print(list(diff))
#
# var = find_mean7(diff)
# print(var)
#
# import math
# stddev = math.sqrt(var)
# print('{:3f}'.format(stddev))
#
#
# import statistics
# print('{:3f}'.format(statistics.pstdev(values)))

# SETS
student_set = set()
student_set.add('Bruno')
student_set.add('Angkush')
student_set.add("Ally")
student_set.add("Shivastav")
student_set.add("Laurent")
print(student_set)

student_set.add("Bruno")
print(student_set)


py_pt_43 = {'Bruno', 'Angkush', "Ally", 'Laurent', 'Shivastav', "Kadeer", "Joeri"}
print(py_pt_43)