#!/Users/kidharb/anaconda3/bin/python3

class Node():
    def __init__(self,parent,position,reachable):
        self.parent = parent
        self.position = position
        self.reachable = reachable

        self.f = 0
        self.g = 0
        self.h = 0

def astar(grid, start, goal):
    openSet = []
    closedSet = []

    startNode = Node(None,start)
    goalNode = Node(None,goal)

    openSet.append(startNode)
    cameFrom = []

    gScore = float('inf')
    fScore = float('inf')

    while len(openSet) > 0:
        current = openSet[0]
        if current == goalNode:
            return #reconstruct path

        closedSet.append(current)
        print(closedSet)



def gen_gridWorld():
    return([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

if __name__ == '__main__':
    rows = 10
    cols = 10
    start = (1, 1)
    goal = (7, 7)
    grid = gen_gridWorld()
    nodes = [[0] * rows for i in range(cols)]

    for i in range(rows):
        for j in range(cols):
            if ((i,j) == start):
                nodes[i][j] = Node(start,(i,j),grid[i][j])
            else:
                nodes[i][j] = Node((0,0),(i,j),grid[i][j])
            print(nodes[i][j].position,nodes[i][j].reachable)
    #astar(grid, start, goal)

