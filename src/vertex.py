class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def connectEdge(self, edge):
        self.edges.append(edge)

    def isNearSink(self):
        numMatched = 0
        for edge in self.edges:
            if edge.getValue(self) == 0:
                numMatched = numMatched + 1
        if numMatched == len(self.edges) - 1:
            return True

    def isNearSource(self):
        numMatched = 0
        for edge in self.edges:
            if edge.getValue(self) == 1:
                numMatched = numMatched + 1
        if numMatched == len(self.edges) - 1:
            return True

    # Move to mark() in edge
    '''
    def denoteUnmarkables(self):
        if self.isNearSink():
            for edge in self.edges:
                if edge.getValue(self) != 0
                    edge.setValue(self, 2)
        if self.isNearSource():
            for edge in self.edges:
                if edge.getValue(self) != 1
                    edge.setValue(self, 2)
    '''
