class Edge:
    def __init__(self, vA, vB):
        self.vA = vA
        self.vB = vB
        self.aValue = 3
        self.bValue = 3

    def getValue(self, vertex):
        if vertex == self.vA:
            return self.aValue
        elif vertex == self.vB:
            return self.bValue

    def setValue(self, vertex, value):
        if vertex == self.vA:
            self.aValue = value
        elif vertex == self.vB:
            self.bValue = value


    # targetVertex is the vertex the edge will be directed towards
    def mark(self, targetVertex):
        if vertex == self.vA:
            if self.aValue == 3:
                self.aValue = 0
                self.bValue = 1
        elif vertex == self.vB:
            if self.bValue == 3:
                self.bValue = 0
                self.aValue = 1

    def toString(self):
        str = 'Edge ' + self.vA.name + self.vB.name + ' '
        if self.aValue == 2 or self.bValue == 2:
            str = str + 'is unmarkable'
        elif self.aValue == 0:
            str = str + 'is marked towards A'
        elif self.bValue == 0:
            str = str + 'is marked towards B'
        elif self.aValue == 3 or self.bValue == 3:
            str = str + 'is unmarked'
        return str
