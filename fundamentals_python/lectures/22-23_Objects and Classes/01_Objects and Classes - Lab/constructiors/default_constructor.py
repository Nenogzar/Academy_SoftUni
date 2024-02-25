# 'Default Constructor'
# (" Default constructors are not defined by the user, "
#  "Python itself creates a constructor during the compilation of the program. "
#  "It doesn’t perform any task but initializes the objects.")
class A():
    check_value = 1000

    def value(self):
        return self.check_value

    def item_content(self):
        return dir(self)

    def item_all_content(self):
        return [item for item in self.item_content()]

    def class_method_names(self):
        return [item for item in self.item_content() if callable(getattr(self, item))]

    def class_attributes(self):
        return [item for item in self.item_content() if not callable(getattr(self, item))]


obj = A()
print(obj.value())
print(f"Class and Object methods: {obj.item_all_content()}")
print(f"Class and Object numbers: {len(obj.item_all_content())}")

print(f"Class methods: {obj.class_method_names()}")
print(f"Class methods number: {len(obj.class_method_names())}")

print(f"Object attributes: {obj.class_attributes()}")
print(f"Object attribute number: {len(obj.class_attributes())}")
