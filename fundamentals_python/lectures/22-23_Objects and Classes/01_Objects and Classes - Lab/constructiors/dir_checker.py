
class dir_check():

    def item_content(self):
        return dir(self)

    def item_all_content(self):
        return [item for item in self.item_content()]

    def class_method_names(self):
        return [item for item in self.item_content() if callable(getattr(self, item))]

    def class_attributes(self):
        return [item for item in self.item_content() if not callable(getattr(self, item))]