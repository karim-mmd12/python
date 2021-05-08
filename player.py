class Player():
    def __init__(self, name, position):
        self.name = name
        self.starting_position = position,
        self.position = self.starting_position

        print(f"{self.name}{self.starting_position}")

    def get_position(self):
        available_position = 0
        return available_position

    def move(self, position):
        self.position = position
