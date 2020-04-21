#!/Users/kidharb/anaconda3/bin/python3

# Pseudocode at https://en.wikipedia.org/wiki/A*_search_algorithm

import gui
from tkinter import *
import heapq

class Node():
    def __init__(self,start,position,goal,reachable):
        if start == position: # The start node
            self.parent = position
            self.gScore = 0
        else:
            self.parent = None
            self.gScore = 99999
        self.position = position
        # reachable tracks whether we can occupy the block or not.
        # we cannot occupy the borders ar any obstacles in the gridworld.
        self.reachable = reachable
        self.fScore = 99999
        
        # heuristic function is the manhattan distance
        self.h = abs(goal[1] - self.position[1]) + abs(goal[0] - self.position[0])


def astar(app, grid, start, goal):

    openSet = set()
    closedSet = set()
    
    # Put the first node on the queue. Use h value as priority
    openSet.add(grid[start[0]][start[1]])
    
    #openSet.put((grid[start[0]][start[1]].h,(start[0],start[1])))
    
    while openSet:
        # extract the Node with the lowest f-score
        current = min(openSet, key=lambda o:o.gScore + o.h)

        if current.position == goal:
            path = []
            while current.parent != 0:
                path.append(current.position)
                current = current.parent
                
            print(path[::-1])
            print("Goal reached - terminating")
            return path[::-1]
        openSet.remove(current)
        #Add it to the closed set
        closedSet.add(current)

        for neighbour in [(grid[current.position[0]+1][current.position[1]]), (grid[current.position[0]][current.position[1]+1]), (grid[current.position[0]-1][current.position[1]]), (grid[current.position[0]][current.position[1]-1])]:
            print(neighbour.position)
            if neighbour in closedSet:
                continue
            if (neighbour.reachable):
                tentative_gScore = current.gScore + 1 # Neighbour so distance from previous node = 1
                if tentative_gScore < neighbour.gScore:
                    neighbour.parent = current
                    neighbour.gScore = tentative_gScore
                    neighbour.fScore = neighbour.gScore + neighbour.h

                    if neighbour not in openSet:
                        openSet.add(neighbour)
                    
    print("Failure : No route to goal from start")
    return

def gen_gridWorld(rows, cols, start, goal, obstacles):
    nodes = [[0] * rows for i in range(cols)]
    print("Parent node : x,y position : heuristic distance : reachable")
    for i in range(rows):
        for j in range(cols):
            if ((i,j) == start):
                nodes[i][j] = Node(start,(i,j),goal,1)
            elif i == 0:
                nodes[i][j] = Node(start,(i,j),goal,0)
            elif i == (rows - 1):
                nodes[i][j] = Node(start,(i,j),goal,0)
            elif j == 0:
                nodes[i][j] = Node(start,(i,j),goal,0)
            elif j == (cols - 1):
                nodes[i][j] = Node(start,(i,j),goal,0)
            elif (i,j) in obstacles:
                nodes[i][j] = Node(start,(i,j),goal,0)
            else:
                nodes[i][j] = Node(start,(i,j),goal,1)    
            print(nodes[i][j].position, nodes[i][j].h)
    return nodes

if __name__ == "__main__" :
    rows = 10
    cols = 10
    gui_cell_size = 50
    start = (6, 1)
    goal = (7, 7)
    obstacles = ((1, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4))

    gridWorld = gen_gridWorld(rows, cols, start, goal, obstacles)

    app = Tk()
    grid = gui.CellGrid(app, rows, cols, gui_cell_size, start, goal, obstacles)
    grid.pack()

    astar(app, gridWorld, start, goal)

    #app.mainloop()

