#########################################################################################
###/ \__/|/  _ \/_   \/  __/  /  __//  __// \  /|/  __//  __\/  _ \/__ __\/  _ \/  __\###
###| |\/||| / \| /   /|  \    | |  _|  \  | |\ |||  \  |  \/|| / \|  / \  | / \||  \/|###
###| |  ||| |-||/   /_|  /_   | |_//|  /_ | | \|||  /_ |    /| |-||  | |  | \_/||    /###
###\_/  \|\_/ \|\____/\____\  \____\\____\\_/  \|\____\\_/\_\\_/ \|  \_/  \____/\_/\_\###
#########################################################################################
import bpy
import random as rnd
 
height = 21; #Maze's area height
width = 21; #Maze's area wodth

height = width #Maze must be square

if width <3 and heidht <3: #Maze must be not less than 3x3
    width =3
    height = 3

#Maze's area height and area width must be odd
height += height%2==0
width += width%2==0
 
#Area's objects
wall = 0; #Wall
visitedCell = 1; #Visited cell
unvisitedCell = 2; #Unvisited Cell

class cell: #Class that keeps cell coordinates
    def __init__(self, x,y):
        self.x=x
        self.y=y;

map = [[wall] * height for i in range(width)] #Area(matrix), where each element is wall

#Generation grid, where each odd element is unvisided cell, and each even element is wall
for i in range(height):
    for j in range(width):
        if i%2 != 0 and j%2 != 0 and i<height and j<width: #if this cell is odd and is within the walls
            map[i][j] = unvisitedCell #then this is unvisited cell
            
def getNeighbours(selectedCell): #Get neighbour cells coordinates
    up = cell(selectedCell.x,selectedCell.y-2) 
    down =  cell(selectedCell.x, selectedCell.y+2)
    left = cell(selectedCell.x-2,selectedCell.y)
    right = cell(selectedCell.x+2, selectedCell.y)
    
    all = [up, down, left, right] #All of the neighbour cells
    neighbours=[] #Neighbour cells that is within the walls
    
    for i in range(4):
        if all[i].x > 0 and all[i].x < width and all[i].y > 0 and all[i].y < height: #if neighbour cell is within the walls 
            neighbours.append(all[i]) #then add it to neighbours
            
    return neighbours

def unvisitedCount(): #Count unvisited cells
    count = 0 #Amount of unvisited cells
    
    for i in range(height):
        for j in range(width): 
            if map[i][j] == unvisitedCell: #if this cell is unvisited
                count+=1 #Up count
                
    print("countdown: ",count) #Print countdown for draw beginning
    
    return count

def DestroyWall(firstCell, lastCell): #Function for destroying the wall
    if lastCell.x - firstCell.x == 2: #If first cell x less than x of last cell then last cell is on right side and first cell is on left side
        map[lastCell.y][lastCell.x-1] = visitedCell #destroy the wall between the cells
        return #exit 
    if lastCell.y - firstCell.y==2: #if first cell y less than last cell y then last cell is upper than first cell 
        map[lastCell.y-1][lastCell.x] = visitedCell #destroy the wall between the cells
        return #Exit
    if firstCell.x - lastCell.x==2: #If last cell x less than first cell x then first cell is on right and last cell is on left
        map[firstCell.y][firstCell.x-1] = visitedCell #destroy the wall between the cells, marking cell as visited
        return #exit the function
    if firstCell.y - lastCell.y==2: #if fitch cell y more than last cell y then first cell is upper
        map[firstCell.y-1][firstCell.x] = visitedCell #destroy the wall between the cells
        return #exit the function

#Generation of the ways
currentCell = cell(rnd.randrange(0,width//2)*2+1,rnd.randrange(0,height//2)*2+1) #select random cell
map[currentCell.y][currentCell.x] = visitedCell #mark selected cell as visited

while unvisitedCount() > 0: #when all of the cells is not visited
    forwardCell = currentCell #mark forward cell as current cell
    
    neighbours = getNeighbours(currentCell) #get neighbour cells
    currentCell = neighbours[rnd.randrange(0,len(neighbours))] #select random cell

    if map[currentCell.y][currentCell.x] != visitedCell: #And if it is unvisited
        DestroyWall(forwardCell, currentCell) #Delete the wall between the forward cell and current cell
        map[currentCell.y][currentCell.x] = visitedCell #And mark this cell as visited
        

#make random holes in the maze
if (rnd.randrange(1)) == 0:
    map[rnd.randrange((height-1)/2)*2+1][0] = visitedCell #bottom side
else:
    map[0][rnd.randrange((width-1)/2)*2+1] = visitedCell #left side
if (rnd.randrange(1)) == 0:
    map[rnd.randrange((height-1)/2)*2+1][width-1]=visitedCell #top side
else: 
    map[height-1][rnd.randrange((width-1)/2)*2+1]=visitedCell #right side

#drawing maze
print("wait for drawing a map");

for i in range(height): 
    for j in range(width): 
        if(map[i][j] == wall):
            bpy.ops.mesh.primitive_cube_add(location=(j*2, i*2, 0)) #create a cube 1x1x1 with location j*2, i*2, 0
                

