from icecream import ic

# file_path = input().split("\\")
# domain_name = file_path[-1]
# file_name, file_extension = domain_name.split('.')
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")

"""whit r and rsplit string """

# file_path = input()
# path = r'{}'.format(file_path)
# directory, full_filename = path.rsplit('\\', 1)
# file_name, file_extension = full_filename.split('.')
#
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")


""" Ivan Shopov"""

# file_path = input().split("\\")
# filename_and_extension = file_path[-1]
# filename, extension = filename_and_extension.split(".")
# print(f"File name: {filename}")
# print(f"File extension: {extension}")

""" """

file_name = input().split(".")
ic(file_name)
file = file_name[0].split("\\")
ic(file)
print(f"File name: {file[-1]}")
print(f"File extension: {file_name[1]}")