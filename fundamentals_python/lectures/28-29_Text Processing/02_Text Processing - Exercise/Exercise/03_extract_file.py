file_path = input().split("\\")
domain_name = file_path[-1]
file_name, file_extension = domain_name.split('.')
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")

"""whit r and rsplit string """

# file_path = input()
# path = r'{}'.format(file_path)
# directory, full_filename = path.rsplit('\\', 1)
# file_name, file_extension = full_filename.split('.')
#
# print(f"File name: {file_name}")
# print(f"File extension: {file_extension}")
