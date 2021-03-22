class Clue(): 

    def __init__(self, x, y, clue, ans, category):
        self.x = x
        self.y = y
        self.clue = clue
        self.ans = ans
        self.category = category

    def getX(self): 
        return self.x

    def getY(self): 
        return self.y

    def getClue(self): 
        return self.clue

    def getAns(self): 
        return self.ans

    def getCat(self):
        return self.category
        