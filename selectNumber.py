
# list of 1 to 10 bc 10 cards max

hand = ['0','0','0','0','0',
        '0','0','0','0','0']
# 0 is empty



# a card has a
# name, cost, damage, type, effect

# card object?

class card:
 """A simple attempt to model a dog."""
    
 def __init__(self, name, cost):
    """Initialize name and age attributes."""
    self.name = name
    self.cost = cost

    def use(self):
        """Use card"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


#  draw pile
strike = card("strike",1)
draw  = [strike,strike]

print(draw)
