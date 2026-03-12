class Player:
    def __init__(self):
        print("Player created")

class Defender:
    def __init__(self):
        print("Defender created")

class Field:
    def __init__(self):
        print("Field loaded")

class Score:
    def __init__(self):
        self.points = 0
        print("Score reset")

class GameController:
    def __init__(self):
        self.field = Field()
        self.score = Score()
        self.player = Player()
        self.defender = Defender()
        print("GameController ready")


print("Starting FIFA STREET...")
game = GameController()