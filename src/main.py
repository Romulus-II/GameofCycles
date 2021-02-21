from vertex import Vertex
from edge import Edge
import sys

def createGame(n):
    vertices = []

    alphabet = 'ABCDEFGHIJ'

    for i in range(n):
        v = Vertex(alphabet[i])
        vertices.append(v)

    for i in vertices:
        for j in vertices:
            if i != j:
                edge = Edge(i, j)
                i.connectEdge(edge)

    print(vertices)

    for i in vertices[0].edges:
        print(i.toString())


def main(argv):
    createGame(3)


if __name__ == '__main__':
    sys.exit(main(sys.argv))
