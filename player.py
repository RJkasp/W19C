class Player:
    def __init__(self, intitalRow, initialColumn):
        self.rowPosition = intitalRow
        self.columnPosition = initialColumn
    
    # movement functions row postion represents up and down. -1 moves player up, +1 moves player down 
    # column position represnts player moving side to side. -1 moves player left and +1 moves player right
    # def moveup
    def moveUp(self):
        self.rowPosition -= 1
    # def movedown
    def moveDown(self):
        self.rowPosition += 1
    # def moveLeft
    def moveLeft(self):
        self.columnPosition -= 1
    # def moveRight
    def moveRight(self):
        self.columnPosition += 1

   

    
