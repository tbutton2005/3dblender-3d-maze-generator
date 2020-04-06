#########################################################################################
###/ \__/|/  _ \/_   \/  __/  /  __//  __// \  /|/  __//  __\/  _ \/__ __\/  _ \/  __\###
###| |\/||| / \| /   /|  \    | |  _|  \  | |\ |||  \  |  \/|| / \|  / \  | / \||  \/|###
###| |  ||| |-||/   /_|  /_   | |_//|  /_ | | \|||  /_ |    /| |-||  | |  | \_/||    /###
###\_/  \|\_/ \|\____/\____\  \____\\____\\_/  \|\____\\_/\_\\_/ \|  \_/  \____/\_/\_\###
#########################################################################################
import bpy
import random as rnd
import numpy as nmp
 
size = 11 #maze size

assert size%2 == 1, 'Error: maze size must be odd.'
 
#Area's objects
wall = 0; #Wall
visitedCell = 1; #Visited cell
unvisitedCell = 2; #Unvisited Cell

class cell: #Class that keeps cell coordinates
    def __init__(self, x,y):
        self.x=x
        self.y=y;

map = nmp.zeros((size,size))
            
def getNeighbours(selectedCell): #Get neighbour cells coordinates
    all =   [       cell(selectedCell.x,selectedCell.y-2), #up
                    cell(selectedCell.x, selectedCell.y+2), #down
                    cell(selectedCell.x-2,selectedCell.y), #left
                    cell(selectedCell.x+2, selectedCell.y) #right
            ] #Neighbour cells
                
    neighbours = [] #neighbour cells within the walls
    
    for neighbourCell in all: #add neighbours that only within the walls
        if neighbourCell.x > 0 and neighbourCell.x < size and neighbourCell.y > 0 and neighbourCell.y < size: #if neighbour cell is within the walls 
            neighbours.append(neighbourCell)
    
    return neighbours
def generate_maze():
    map = nmp.zeros((size,size))#Area(matrix), where each element is wall
    map[1::2, 1::2] = unvisitedCell #Generate a grid, where each odd element is unvisided cell, and each even element is wall

    def isUnvisitedCells(): #Count unvisited cells
        for line in map:
            if unvisitedCell in line:
                return True
    
        return False

    #Generation of the ways
    currentCell = cell(rnd.randrange(1,size-2, 2),rnd.randrange(1,size-2, 2)) #select random cell

    while isUnvisitedCells(): #when all of the cells is not visited
        forwardCell = currentCell #mark forward cell as current cell
    
        currentCell = rnd.choice(getNeighbours(currentCell)) #select random neighbour cell

        if map[currentCell.y][currentCell.x] != visitedCell: #And if it is unvisited
            map[currentCell.x-int((currentCell.x-forwardCell.x)/2)][currentCell.y-int((currentCell.y-forwardCell.y)/2)] = visitedCell #Delete the wall between the forward cell and current cell
            map[currentCell.y][currentCell.x] = visitedCell #And mark this cell as visited
        

    #make random holes in the maze
    map[0][rnd.randrange(1,size-1,2)] = visitedCell
    map[size-1][rnd.randrange(1,size-1,2)] = visitedCell

    #drawing maze
    print("wait for drawing a map");

    for i in range(size): 
        for j in range(size): 
            if(map[i][j] == wall):
                bpy.ops.mesh.primitive_cube_add(location=(j*2, i*2, 0)) #create a cube 1x1x1 with location j*2, i*2, 0
                

