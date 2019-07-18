class GameCell:
    
    def __init__(self, row, col, alive = True):
        self.row = row
        self.col = col
        self.around = 0
    
    def __eq__(self, value):
        return (self.row, self.col) == (value.row, value.col)
    
    def create(self):
        self.alive = True
        self.around = 0
        return self
    
class GameGrid:
    def __init__(self, width, height):
        self.rowMax = width
        self.colMax = height
        self.cells = []
        self.deltas = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1,1), (-1, 0)]
        
    def create_new_cells(self):
        """
        create new cells
        """
        newCells = self.cells[:]
