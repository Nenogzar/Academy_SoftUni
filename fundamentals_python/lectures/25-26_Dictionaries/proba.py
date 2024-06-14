# def get_magic_triangle(n):
#
#     triangle = [[1], [1, 1]]
#
#     for i in range(2, n):
#         last_row = i - 1
#         new_row = [1]
#         for j in range(1, i):
#             last_col = j - 1
#             new_row.append(triangle[last_row][last_col] + triangle[last_row][j])
#         new_row.append(1)
#         triangle.append(new_row)
#     return triangle
#############################################################################################
# def get_magic_triangle(n):
#     result = [[1], [1, 1]]
#
#     if n <= 2:
#         return result[:n]
#
#     for row in range(2, n):
#         last_row = result[row - 1]
#         new_row = [1]
#         for index in range(1, len(last_row)):
#             new_row.append(last_row[index - 1] + last_row[index])
#         new_row.append(1)
#         result.append(new_row)
#
#     return result

###################################################################################################

# def get_magic_triangle(n):
#     # Инициализираме триъгълника с първите два реда
#     triangle = [[1], [1, 1]]
#
#     # Генерираме следващите редове до достигане на n реда
#     for i in range(2, n):
#         new_row = [1]  # Новият ред започва с 1
#         for j in range(1, i):
#             # Проверяваме дали индексите са валидни, преди да достъпим елементите
#             if 0 <= j - 1 < len(triangle[i - 1]) and 0 <= j < len(triangle[i - 1]):
#                 new_row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
#         new_row.append(1)  # Новият ред завършва с 1
#         triangle.insert(1, new_row)  # Вмъкваме новия ред на втора позиция, за да запазим изграждането отгоре надолу
#
#     return triangle

###################################################################################################





