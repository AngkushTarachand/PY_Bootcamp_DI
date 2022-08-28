import math



list_of_D = list(map(int, input("Enter number").split(', ')))
print(list_of_D)

for D in list_of_D:
    C = 50
    H = 30
    print(D, type(D))
    Q = math.sqrt((2*C*D)/H)
    print(Q)


