class Player:
    def __init__(self, position = 0):
        self.position = position

    # Add a move() method with steps parameter
    def move(self, steps):
        self.position = steps
        return self.position

    def result(self):
        return self.position


player1 = Player()
print('player1 results')
print(player1.move(2))
print(player1.result())

p2 = Player()
print('p2 results')
print(p2.result())