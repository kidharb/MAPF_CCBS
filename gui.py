#!/Users/kidharb/anaconda3/bin/python3

from tkinter import *

class Cell():
    def __init__(self, master, x, y, size, fillColourBG, fillBorder):
        """ Constructor of the object called by Cell(...) """
        self.master = master
        self.abs = x
        self.ord = y
        self.size= size
        self.fill= False
        self.fillcolour= fillColourBG
        self.fillborder= fillBorder

    def _switch(self):
        """ Switch if the cell is filled or not. """
        self.fill= not self.fill

    def draw(self):
        """ order to the cell to draw its representation on the canvas """
        if self.master != None :
            fill = self.fillcolour
            outline = self.fillborder

            xmin = self.abs * self.size
            xmax = xmin + self.size
            ymin = self.ord * self.size
            ymax = ymin + self.size

            self.master.create_rectangle(xmin, ymin, xmax, ymax, fill = fill, outline = outline)

class CellGrid(Canvas):
    def __init__(self,master, rowNumber, columnNumber, cellSize, start, goal, obstacles, *args, **kwargs):
        Canvas.__init__(self, master, width = cellSize * columnNumber , height = cellSize * rowNumber, *args, **kwargs)

        fillColourBG = "white"
        fillBorder = "black"

        self.cellSize = cellSize

        self.grid = []
        for row in range(rowNumber):

            line = []
            for column in range(columnNumber):
                line.append(Cell(self, column, row, cellSize, fillColourBG, fillBorder))
                if (row,column) == start:
                    line.append(Cell(self, column, row, cellSize, "yellow", fillBorder))
                if (row,column) == goal:
                    line.append(Cell(self, column, row, cellSize, "lightgreen", fillBorder))
                if row == 0:
                    line.append(Cell(self, column, row, cellSize, "black", fillBorder))
                if row == (rowNumber - 1):
                    line.append(Cell(self, column, row, cellSize, "black", fillBorder))
                if column == 0:
                    line.append(Cell(self, column, row, cellSize, "black", fillBorder))
                if column == (columnNumber - 1):
                    line.append(Cell(self, column, row, cellSize, "black", fillBorder))
                if (row,column) in obstacles:
                    line.append(Cell(self, column, row, cellSize, "black", fillBorder))
            self.grid.append(line)

        #memorize the cells that have been modified to avoid many switching of state during mouse motion.
        self.switched = []

        #bind click action
        self.bind("<Button-1>", self.handleMouseClick)
        #bind moving while clicking
        self.bind("<B1-Motion>", self.handleMouseMotion)
        #bind release button action - clear the memory of midified cells.
        self.bind("<ButtonRelease-1>", lambda event: self.switched.clear())

        self.draw()



    def draw(self):
        for row in self.grid:
            for cell in row:
                cell.draw()

    def _eventCoords(self, event):
        row = int(event.y / self.cellSize)
        column = int(event.x / self.cellSize)
        return row, column

    def handleMouseClick(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]
        cell._switch()
        cell.draw()
        #add the cell to the list of cell switched during the click
        self.switched.append(cell)

    def handleMouseMotion(self, event):
        row, column = self._eventCoords(event)
        cell = self.grid[row][column]

        if cell not in self.switched:
            cell._switch()
            cell.draw()
            self.switched.append(cell)


if __name__ == "__main__" :
    rows = 10
    cols = 10
    cell_size = 50
    start = (6, 1)
    goal = (7, 7)
    obstacles = ((1, 4), (3, 4), (4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (9, 4))
    #grid_ascii = gen_gridWorld()
    nodes = [[0] * rows for i in range(cols)]

    app = Tk()
    grid = CellGrid(app, rows, cols, cell_size, start, goal, obstacles)
    print(grid)
    grid.pack()

    app.mainloop()

