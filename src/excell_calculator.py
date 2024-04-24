# Implement a simplified Excel Calculator with the following methods:

# set(id: string, expression: string[]): void
# This will set the cell equal to the sum of expression values.
# The expression values will either be integer strings like ('1', '2', '12') or cell ids like ('A1', 'B1', 'C12'), where cell ids are a character followed by an integer value.

# get(id: string): int
# This returns the value for the cell by its id.

# Example:
# set('A1', ['1']) -> A1 = 1
# set('B1', ['1', 'A1']) -> B1 = 2  = 1 + A1
# set('A1', ['3']) -> A1 = 3 AND B1 = 4
# get(‘A1’) -> 3 
# get(‘B1’) -> 4 

class Calculator:
    def __init__(self):
        self.cells = dict()
        self.computed = dict()
        self.dependencies = dict()
    
    
    def invalidate(self, cellId: str):
        # A1 -> []
        # B1 -> [A1]
        # C1 -> [B1]
        # xxx -> [C1] - no
        
        # A1
        # B1
        if cellId in self.computed:
            del self.computed[cellId]
            
        for depId, depCells in self.dependencies.items():
            # depId = B1, [A1]
            if cellId in depCells:
                self.invalidate(depId)

                
    def setCell(self, cellId: str, epxression: list):
        if type(epxression) is not list:
            raise ValueError("expression has to be an array")

        self.cells[cellId] = epxression
        self.dependencies[cellId] = list(filter(lambda x: type(x) is str, epxression))
        self.invalidate(cellId)

    def computeCell(self, cellId: str):
        if cellId not in self.cells:
            raise KeyError(f"not such a cell {cellId}")

        expression = self.cells[cellId]
        result = 0
        for item in expression:
            if type(item) is int:
                result += item
            else:
                result += self.getCell(item)
    
        return result
        
    def getCell(self, cellId: str):
        if cellId not in self.computed:
            self.computed[cellId] = self.computeCell(cellId)
        return self.computed[cellId]


c = Calculator()
c.setCell('A1', [1])
c.setCell('B1', [1, 'A1'])
assert c.getCell('B1') == 2
assert c.getCell('A1') == 1
c.setCell('A1', [3])
assert c.getCell('A1') == 3
assert c.getCell('B1') == 4
  
