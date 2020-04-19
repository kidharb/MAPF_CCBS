import gui
from tkinter import *

class Node():
    def __init__(self,parent,position,goal,reachable):
        self.parent = parent
        self.position = position
        self.reachable = reachable

        self.f = 0
        self.g = 0
        self.h = abs(goal[1] - self.position[1]) + abs(goal[0] - self.position[0])

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

def gen_gridWorld(rows, cols, start, goal, obstacles):
     nodes = [[0] * rows for i in range(cols)]
     print("Parent node : x,y position : heuristic distance : reachable")
     for i in range(rows):
         for j in range(cols):
             nodes[i][j] = Node((0,0),(i,j),goal,1)
             if ((i,j) == start):
                 nodes[i][j] = Node(start,(i,j),goal,1)
             if i == 0:
                 nodes[i][j] = Node((0,0),(i,j),goal,0)
             if i == (rows - 1):
                 nodes[i][j] = Node((0,0),(i,j),goal,0)
             if j == 0:
                 nodes[i][j] = Node((0,0),(i,j),goal,0)
             if j == (cols - 1):
                 nodes[i][j] = Node((0,0),(i,j),goal,0)
             if (i,j) in obstacles:
                 nodes[i][j] = Node((0,0),(i,j),goal,0)


             print(nodes[i][j].parent,nodes[i][j].position,nodes[i][j].h,nodes[i][j].reachable)

if __name__ == "__main__" :
     rows = 10
     cols = 10
     cell_size = 50
     start = (6, 1)
     goal = (7, 7)
     obstacles = ((1, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4))

     gridWorld = gen_gridWorld(rows, cols, start, goal,  obstacles)

     app = Tk()
     grid = gui.CellGrid(app, rows, cols, cell_size, start, goal, obstacles)
     grid.pack()

     app.mainloop()

