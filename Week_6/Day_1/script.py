print("This is my first python script.")

# Basic Value type
print(type(1))         # int
print(type('1'))        # str
print(type(False))      # bool
print(type('False'))    # str
print(type(1.25))       # float

# Strings
print("Hello World")
print('Hello World')

# String in-built function (methods)
print('hello World'.capitalize())
print('hello World'.lower())
print('Hello World'.upper())
print('Hello World'.replace('hello', 'hi'))
print('hello world'.index('h'))
print('hello world'.startswith('hello'))

# Number - Integers(int - whole numbers) and Float(float - point numbers)
print(type(1))
print(type(1.0))

# Arithmetic operations
print(3+4)      # Addition
print(3-4)      # Subtraction
print(3*4)      # Multiplication
print(4/3)      # Division
print(4//3)     # Floor division
print(4 % 3)      # Remainder (Modulus) of (4/3)

# Type Casting - convert a type to another
print('12' * 2)
print('12' + str(2))        # Concatenate string
print(int('12')+2)          # Addition
# We can only add value of the same type (str + str Or number + number)
# We cannot add string and number

# Special characters
print("Today is Monday. \n This evening is quite chilly")
print("Group \t\t\t Student 1 \t Student 2")
print("Cool as Cool \t\t Joeri \t\t Bruno")
print("WestTech \t\t Laurent \t Angkush")
print("FunRunGame \t\t Ally \t\t Shivastav")

# Booleans - True or False
print(True)
print(False)
# Does not exit
# print(true)
# print(false)

print(int(True))        # 1
print(int(False))       # 0
print(str(True))        # 'True'
print(str(False))       # 'False'

print('HELLO'.isupper())  # True
print(3 < 2)              # False

# Comparisons
# < - Less than
# > - Greater than
# = - Assign
# == - Equal to
# != - Not equal to
# <= - Less than or equal
# >= - Greater than or equal

print(6 == 6)
print(6 is 6)
print(6 is not 5)   # 6 != 5

# Booleans function
print(bool(5))
print(bool(0))
print(bool(-2))
print(bool('Hello'))
