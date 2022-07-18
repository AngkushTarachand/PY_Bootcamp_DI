# ---------------- Exercise 9 ----------- #

NumOfPeople = input("Enter the numer of people ")
NumOfPeople = int(NumOfPeople)
x = 0
counter1 = 0
counter2 = 0
counter3 = 0

while x < NumOfPeople:
    age = input("Enter the age of the person")
    age = int(age)
    if age < 3:
        print("The ticket is free")
        counter1 = counter1 + 1
    elif 3 <= age <= 12:
        print("The ticket is $10")
        counter2 = counter2 + 1
    else:
        print("The ticket is $15")
        counter3 = counter3 + 1
    x = x + 1

Total = counter1*0 + counter2*10 + counter3*15
print("The total is {}".format(Total))

name_list = ["Raj", "Ram", "Abhi"]
for teenager in name_list:
    age1 = int(input("Please enter {} age".format(teenager)))
    if 16 <= age1 <= 21:
        name_list.remove(teenager)
print(name_list)
