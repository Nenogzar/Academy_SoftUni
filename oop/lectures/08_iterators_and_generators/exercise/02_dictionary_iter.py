class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.dictionary):
            items = self.dictionary[self.idx]
            self.idx += 1
            return items
        raise StopIteration

# class dictionary_iter:
#     def __init__(self, dictionary: dict):
#         self.dict_tuple = tuple(dictionary.items())
#         self.idx = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.idx < len(self.dict_tuple):
#             idx = self.idx
#             self.idx += 1
#             return  self.dict_tuple[idx]
#         raise StopIteration





result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
print("--------------------------------")

result1 = dictionary_iter({"name": "Peter", "age": 24})
for y in result1:
    print(y)
