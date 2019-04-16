# this document is to set up the card superclass and sublasses for our game

class Card:
    def __init__(self, Name='', Cost=0):
        self.Name = Name
        self.Cost = Cost
    
    def GetName(self):
        return self.Name
    def SetName(self,Name):
        self.Name = Name

    def GetCost(self):
        return self.Cost
    def SetCost(self,Cost):
        self.Cost = Cost

class ActionCard(Card):
    def __init__(self,Name, Cost, Ability):
        super().__init__(Name, Cost, Ability)

