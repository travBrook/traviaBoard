"""TriviaBoard is built using Python and PyQt5."""

import sys, ast, pdb

# Import QApplication and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFrame, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QGridLayout, QVBoxLayout

triviaInfo = {}
doubleTriviaInfo = {}
catColumns = {}
doubleCatColumns = {}

__version__ = '0.1'

# Create a subclass of QMainWindow to setup the board's GUI
class TriviaBoardUi(QMainWindow):
    """TriviaBoard's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Ds Trivia')

        #self.setFixedSize(550, 550)  # Change this 
        
        # Set the central widget
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self.setStyleSheet('background-color : red')
        # Set layouts of different parts
        self.generalLayout = QVBoxLayout()
        
        self.createCategories()
        #self.createClues()

        self._centralWidget.setLayout(self.generalLayout)


    #Creates the category labels and adds them to the general layout. 
    def createCategories(self):
        pass
        #NOTE might want to store the category labels in case they need to change or whatever.
        #
        self.categories = {}
        categoriesLayout = QHBoxLayout()
        for category, clues in triviaInfo.items():
            pass
            theLabel = QLabel(category)
            theLabel.setFrameShape(QFrame.Box)
            theLabel.setLineWidth(2)
            theLabel.setFixedSize(150, 100)
            theLabel.setStyleSheet('background-color : blue')
            categoriesLayout.insertWidget(int(clues[0][0]), theLabel)
            self.categories[category] = theLabel
        
        self.generalLayout.addLayout(categoriesLayout)

    #Creates buttons with dollar amounts on them under the corresponding category 
    def createClues(self):
        #Have the key for the clues be the coordinates for it? 
        self.clues = {}
        clueLayout = QGridLayout()
        # Button text | position (x,y) 
        buttons = {
            #Col 1
            '200': (0, 0),
            '400': (0, 1),
            '600': (0, 2),
            '800': (0, 3),
            '1000': (0, 4),
            #Col 2
            '200': (1, 0),
            '400': (1, 1),
            '600': (1, 2),
            '800': (1, 3),
            '1000': (1, 4),
            #Col 3
            '200': (2, 0),
            '400': (2, 1), 
            '600': (2, 2),
            '800': (2, 3),
            '1000': (2, 4),
            #Col 4
            '200': (3, 0),
            '400': (3, 1),
            '600': (3, 2),
            '800': (3, 3),
            '1000': (3, 4),
            #Col 5
            '200': (4, 0),
            '400': (4, 1),
            '600': (4, 2),       
            '800': (4, 3),
            '1000': (4, 4),
            #Col 6
            '200': (5, 0),
            '200': (5, 1),
            '200': (5, 2),
            '200': (5, 3),
            '200': (5, 4),
        }
        # Create the buttons and add them to the grid layout
        for btnText, pos in buttons.items():
            #TUPLE that holds (button, (x,y,clue,ans)) (should probably make clue object)
            theCat = catColumns[pos[0]+1]
            theClue = []
            for clue in triviaInfo[theCat] : 
                if (pos[1]+1) == clue[1] : 
                    theClue = clue
                    break
            self.clues[pos] = (QPushButton(btnText), theClue)  
            theButton = self.clues[pos][0]
            theButton.setFixedSize(150, 100)
            theButton.setStyleSheet('background-color : blue; color : yellow')

            clueLayout.addWidget(theButton, pos[1], pos[0]) #NOTICE the y, x positioning

        # Add buttonsLayout to the general layout
        self.generalLayout.addLayout(clueLayout)


'''
Goes through given text file in specific format (see show #4596 txt)
and finds the categories, and makes a dictionary linking the category 
to a quadruple : (x, y, clue, answer) 
'''
def populateData(inputFile):
    pass
    f = open(inputFile, "r")
    my_text = f.readlines()[1:] #reads to whole text file, skipping first 4 lines
    for count, line in enumerate(my_text): 
        if line == '\n' : 
            pass
        elif count == 1 : 
            categories = ast.literal_eval(line)

            for count2, cat in enumerate(categories): 
                if count2 <= 5 :
                    triviaInfo[cat] = []
                else :
                    doubleTriviaInfo[cat] = []

        else : 
            #Separate double jeopardy
            if count >= 33 : 
                clueInfo = line.split("  8==D  ")
                theCat = clueInfo[2]
                x = clueInfo[0]
                y = clueInfo[1]
                clue = clueInfo[3]
                ans = clueInfo[4]
                doubleTriviaInfo[theCat].append((x,y,clue,ans))
                if x not in doubleCatColumns.keys() : 
                    print(x)
                    doubleCatColumns[x] = theCat
            else : 
                clueInfo = line.split("  8==D  ")
                theCat = clueInfo[2]
                x = clueInfo[0]
                y = clueInfo[1]
                clue = clueInfo[3]
                ans = clueInfo[4]
                triviaInfo[theCat].append((x,y,clue,ans))
                if x not in catColumns.keys() : 
                    print(x)
                    catColumns[x] = theCat
            

# Client code
def main():
    """Main function."""
    # Create an instance of QApplication
    triviaBoard = QApplication(sys.argv)
    # Show the board's GUI
    view = TriviaBoardUi()
    view.show()
    # Execute the board's main loop
    sys.exit(triviaBoard.exec_())

if __name__ == '__main__':
    populateData("Show #4596 - Monday, September 6, 2004.txt")#sys.argv[1])
    main()