try:
    f = open("secrets.txt", mode="w+")
    f.write("123")

    num = int(input("Please enter a number"))
    print(10/num)

finally:
    print("closing")
    f.close()

