# f = open('secrets.txt', mode='a+')
# # r - read
# # w - write
# #
# f.write("abc")
# content = f.read()
# print(content)
# f.write("abc")
#
# print(1, f.write("abc"))
# f.close()
# print(2, f.close())
# #

# print(content)

f = open("secrets.txt", mode="a+")
print(f.tell())
f.seek(3)

f.write("000000")

f.close()
