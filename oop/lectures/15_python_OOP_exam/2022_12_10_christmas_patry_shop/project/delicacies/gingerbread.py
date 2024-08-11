from project.delicacies.delicacy import Delicacy
class Gingerbread(Delicacy):
    _portion = 200
    def __init__(self,name: str, price: float):
        super().__init__(name: str, self._portion, price: float):
