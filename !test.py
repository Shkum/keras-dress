import os
print(*list(os.walk(r"D:\ps2")), sep='\n')
# for root, directories, files in os.walk(r"D:\ps2"):
#     print(files)
#     for directory in directories:
#         print(directory)
#     for file in files:
#         print(file)
#         print()


