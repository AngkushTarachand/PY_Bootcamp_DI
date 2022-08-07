# with open("download.txt") as f:
#     for line_number, line in enumerate(f):
#         if line_number == 5:
#             print(line)
#
# with open("download.txt") as f:
#     print(f.read(5))
#
# with open("download.txt") as f:
#     lines = f.readlines()
#     lines = list(map(lambda line: line.rstrip(), lines))
#     print(lines)
#
#     print(lines.count("Darth"))
#     print(lines.count("Luke"))
#     print(lines.count("Lea"))

lines = []
with open("download.txt") as f:
    lines = f.readlines()
    lines = list(map(lambda line: line.rstrip(), lines))

with open("download.txt", "w") as f:
    for name in lines:
        if name == "Lukes":
            pass