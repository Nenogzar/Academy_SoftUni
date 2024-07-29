from typing import List

from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self):
        self.decorations: List[BaseDecoration] = []

    def add(self, decoration: BaseDecoration):
        """
        Adds a decoration object to the list.
        :param decoration: The decoration object to add.
        """
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        """
        Removes a decoration object from the list if it exists.
        :param decoration: The decoration object to remove.
        :return: True if the decoration was removed, False otherwise.
        """
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        """Returns the first decoration of the given type if there is.
        Otherwise, returns a message "None"
        """
        for dec in self.decorations:
            if type(dec).__name__ == decoration_type:
                return dec
        return "None"
