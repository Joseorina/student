class Matrix:
    def __init__(self):
        """
        Initialize an empty array
        """
        self.matrix = []
        self.rows = 0
        self.columns = 0
        self.name = ' '
        
    def __str__(self):
        """
        
        """
        return self.matrix
    
    def create_matrix(self, rows, columns, v=False):
        self.rows = rows
        self.columns = columns
        self.matrix = [[(row, col) for col in range(columns)] for row in range(rows)]
        if v == True:
            print('Created a {self.row} rows by {self.columns} columns matrix')
            print('---' * columns)
            self.printer()
            print('-----'*columns)
    
    def printer(self, v=False):
        if v == True:
            print('a {self.row} by {self.columns} matrix')
        for row in self.matrix:
            print(row)
            
    def get_row(self, n, v =False):
        if v == False:
            print('matrix [row{n}..')
            print(self.matrix(n))
        return self.matrix[n]
    
    def get_column(self, n, v = False):
        i = 0
        items = []
        while i < self.rows:
            items.append(self.matrix[i][n])
            i += 1
        if v == True:
            print('matrix[col={n}]..')
            for item in items:
                print(item)
        return items
