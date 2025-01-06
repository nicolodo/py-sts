# This file is about setting up cards a class

# each card will be an object

class card():
    """This is the card class"""
    
    def __init__(self, name, cost, atk, block):
        """Card model"""
        self.name = name
        self.cost = cost
        self.atk = atk
        self.block = block

    def playCard(self):
        print(f"you have played {self.name} for {self.cost}")
        print(f"it has done {self.atk} attack and provided {self.block} block")

strike = card("strike",1,6,0)
strike.playCard()
