# creatures have hp and status effects

# save info in format
# name,hp,vl

# if enemy then have a attack pattern and next attack

class creature():
    """The player and enemies"""

    def __init__(self,hp,name,voiceLine):
        self.hp = hp
        self.name = name
        self.vline = voiceLine

    def call(self):
        print(self.vline)

    def stats(self):
        print(f"hp:{self.hp}")
        print(self.name)

class enemy():
    """what the player fights"""

    def __init__(self,actionStateMachine):
        self.asm = actionstatemachine
#        self.properties = creature( # idk a tuple?)

    def getNextAction(self):
        # get present action, decide next one
        self.nAct = 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 80 #idk 
        
ironclad = creature(80,"ironclad","caw caw!")
ironclad.stats()
ironclad.call()
