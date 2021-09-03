# import os  
# import shutil

# # source = "C:\\Users\\OM\\Desktop\\test"
# # destination = "C:\\Users\\OM\\Desktop\\anonymous"
# # # dest = shutil.copy(source, destination)
# # # path = "C:\\Users\\OM\\Desktop\\test"

# # # print("Files after coping\n")
# # # dest = shutil.move(source , destination)

# # path = "C:\\Users\\OM\\Desktop"
# # print("Files after coping\n")
# # print(os.listdir(destination))

# path  = input("Enter the path...\n")
# list  = os.listdir(path)

# for file in list:
#     name, ext = os.path.splitext(file)
#     ext = ext[1:]
#     if ext == "":
#         continue
#     if os.path.exists(path + "/" + ext):
#         shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
#     else:
#         os.makedirs(path + "/" + ext)
#         shutil.move(path + "/" + file, path + "/" + ext + "/" + file)
