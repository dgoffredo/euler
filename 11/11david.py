#!/usr/bin/env python3

# This program snakes along the input grid with a 'ray' of a specified
# length, and finds the greatest product of numbers among those that the ray
# covers at any moment over its journey.
#
# The 'sheets' that the ray covers look like this:

# ---------    | | | |     ////  
# ---------    | | | |     ///   (and the other three rotations for the corners)
# ---------    | | | |     //
# ---------    | | | |     /

from sys import argv, stdin
from operator import mul # mul is the product, i.e. 6 == mul(2, 3)
from functools import reduce
# So, reduce(mul, [2, 5, 3]) would be 
# mul(mul(2, 5), 3) = (2 * 5) * 3 = 2 * 5 * 3 = 30

#
# Inputs:
# 
#  file $1:    - Whitespace-separated columns of numbers in text,
#                in newline-separated rows.
#              - The resulting grid must be square.
#  
#     stdin:   - Number of terms in a product.
#              - Must be less than the side length
#              - of the grid.  
#
# This algorithm checks the center diagonals
# multiple times, but could be modified to prevent
# that pretty easily.


# For extracting "(x, y): value" from file
def parseGridIter(inputFile):
    for y, line in enumerate(inputFile.readlines()):
        for x, word in enumerate(line.split()):
            yield ( (x, y), int(word) )

# Aggregates into a dictionary the result of iterating over the parser
def parseGrid(inputFile):
    return dict(parseGridIter(inputFile))

# Has to be square, and returns size
def checkGrid(grid):
    xMax = max(x for x, y in grid.keys())
    yMax = max(y for x, y in grid.keys())

    assert xMax == yMax
    return xMax + 1
   
filename = argv[2] if len(argv) > 2 else '<stdin>'
grid = parseGrid(open(filename) if len(argv) > 2 else stdin)
gridSize = checkGrid(grid)

rayLen = int(input()) if len(argv) < 2 else int(argv[1]) # int(input('Number of terms in each product: '))
assert rayLen <= gridSize and 0 < rayLen

# Vector addition
def advance(point, direction, times=1):
    (x, y) = point
    (dx, dy) = direction
    return (x + times*dx, y + times*dy)

def getX(point): # for convenience
    x, y = point
    return x
def getY(point): # for convenience
    x, y = point
    return y

# An iterable series of values in the grid
def pathValues(grid, start, delta, length):
    yield grid[start]
    pos = start
    for _ in range(length-1):
        pos = advance(pos, delta)
        yield grid[pos]

# Product of the values along the length of a ray
def product(grid, start, delta, size):
    return reduce(mul, (num for num in pathValues(grid, start, delta, size)))

# Returns a function that tells you if a point is in the grid
def validPointChecker(gridSize):
    def validPoint(point):
        (x, y) = point
        return 0 <= x and x < gridSize and 0 <= y and y < gridSize
    return validPoint

validPoint = validPointChecker(gridSize) # for our grid

# Get the maximum product for a certain pass through the grid.
# col means 'column'
# note: colLen should be a function that takes a point.
def sheetMax(grid, colStart, colLen, rowDelta, rayLen, rayDelta):
     totalMax = 0
     while validPoint(colStart):
         tail = colStart
         head = advance(tail, rayDelta, rayLen - 1)
         colMax = product(grid, tail, rayDelta, rayLen)

         for _ in range(colLen(colStart) - rayLen):
             newHead = advance(head, rayDelta)
             newTail = advance(tail, rayDelta)
             if grid[newHead] > grid[tail]:
                 colMax = product(grid, newTail, rayDelta, rayLen)
             head, tail = newHead, newTail
         
         totalMax = max(totalMax, colMax)
         colStart = advance(colStart, rowDelta)
     return totalMax

# Height functions
#
def straightHeight(gridSize):
    return lambda _ : gridSize # independent of row or column

def leftDiagsHeight(p):
    return getX(p) + 1

def rightDiagsHeight(gridSize):
    return lambda p: gridSize - getX(p)

#
# The "sheets", or ways in which we zig-zag over the grid.
#
#          (  begin,                                         heightFunc, rowDelta, rayDelta  )  
sheets = [ (  (0,0),                           straightHeight(gridSize),    (0,1),    (1, 0)  ),  # by rows
           (  (0,0),                           straightHeight(gridSize),    (1,0),    (0, 1)  ),  # by columns
           (  (rayLen-1, 0),                            leftDiagsHeight,    (1,0),   (-1, 1)  ),  # bottom left  diag
           (  (rayLen-1, gridSize-1),                   leftDiagsHeight,    (1,0),   (-1,-1)  ),  #    top left  diag
           (  (gridSize-rayLen, 0),          rightDiagsHeight(gridSize),   (-1,0),    (1, 1)  ),  # bottom right diag
           (  (gridSize-rayLen, gridSize-1), rightDiagsHeight(gridSize),   (-1,0),    (1,-1)  ) ] #    top right diag

gridMax = max(sheetMax(grid, begin, heightFunc, 
                       rowDelta, rayLen, rayDelta) for begin, heightFunc, rowDelta, rayDelta in sheets)

# print('\nGreatest product of {} adjacent numbers in the grid is {}'.format(rayLen, gridMax))
print(gridMax)


