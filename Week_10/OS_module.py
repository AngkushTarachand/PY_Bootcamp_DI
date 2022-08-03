# import os
#
# for x in range(1, 6):
#     x = str(x)
#     directory = "week" + x
#
#     print(directory)
#
#     parent_dir = "C:\Users\Angkush Tarachand\PY_Bootcamp_DI"
#
#     path = os.path.join(parent_dir, directory)
#
#     for day in range(1, 6):
#         day = str(day)
#         directory_day = "day" + day
#
#         print(directory_day)
#
#         sub_parent_dir = f"C:\Users\Angkush Tarachand\PY_Bootcamp_DI\{directory}"
#
#         path1 = os.path.join(sub_parent_dir, directory)
#
#         for each in day:
#             directory
#

import os

for i in range(1, 6):
    os.mkdir(f'Week{i}')
    for j in range(1, 6):
        os.makedirs(f'Week{i}/Day{j}/lesson')
        os.mkdir(f'Week{i}/Day{j}/homework')
