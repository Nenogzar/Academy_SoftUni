class reverse_iter:
    def __init__(self, iterible):
        self.iterible = iterible

    def __iter__(self):
        return reversed(self.iterible)


# class reverse_iter:
#     def __init__(self, args):
#         self.args = args
#         self.current = len(self.args)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current == 0:
#             raise StopIteration
#         self.current -= 1
#         return self.args[self.current]


# class reverse_iter:
#     def __init__(self, iterible):
#         self.iterible = iterible
#         self.current_idx = len(self.iterible)
#         self.stop_idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.current_idx -= 1
#         if self.current_idx >= self.stop_idx:
#             return self.iterible[self.current_idx]
#         raise StopIteration

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
