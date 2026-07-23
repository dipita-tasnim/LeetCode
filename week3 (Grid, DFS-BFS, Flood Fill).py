# Flood Fill

# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill:
# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation:
# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation:
# The starting pixel is already colored with 0, which is the same as the target color. Therefore, no changes are made to the image.

# for better understanding:

# The rules: 
# Start at pixel (sr, sc). Note its original color.
# Change it to the new color.
# Spread to its 4 neighbors (up, down, left, right — NOT diagonal).
# A neighbor only gets painted if it has the same original color.
# Keep spreading from each newly painted pixel until nothing more matches.
# Walk through Example 1

# image = [[1,1,1],
#          [1,1,0],
#          [1,0,1]]
# start = (1,1), new color = 2
# Step 1: Look at the starting pixel (1,1) → its value is 1. So original color = 1. We'll paint every connected 1 into 2.


# 1  1  1
# 1 [1] 0        ← start here (row 1, col 1)
# 1  0  1
# Step 2: Paint it, then spread to connected 1s:


# 2  2  2        ← all these 1s were connected → painted
# 2  2  0        ← the 0 blocks the spread (different color)
# 2  0  1        ← this 1 is CUT OFF by the 0s around it
# Result: [[2,2,2],[2,2,0],[2,0,1]]


# Using Recursion

def floodFill(image, sr, sc, color):
    original = image[sr][sc]

    if original == color:
        return image  # as per example 2
    
    def fill(r, c):

        # stop if outside the grid
        if r < 0 or r >= len(image) or c < 0 or c>= len(image[0]):
            return
        
        # stop if this pixel is not the original color
        if image[r][c] != original:
            return
        
        image[r][c] = color  # paint it

        fill(r + 1, c)       # spread down
        fill(r - 1, c)       # spread up
        fill(r, c + 1)       # spread right
        fill(r, c - 1)       # spread left

    fill(sr, sc)
    return image

print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))


# Or --------- Using Stack

def floodFill(image, sr, sc, color):
    original = image[sr][sc]

    if original == color:
        return image
    
    rows = len(image)
    cols = len(image[0])
    stack = [(sr, sc)]    # to do list

    while len(stack) > 0:
        r, c = stack.pop()

        # skip if outside the grid
        if r < 0 or r>= rows or c < 0 or c >= cols:
            continue

        # skip if wrong color
        if image[r][c] != original:
            continue

        image[r][c] = color   # paint it

        stack.append((r + 1, c))
        stack.append((r - 1, c))    
        stack.appen((r, c + 1))
        stack.appen((r, c - 1))

    return image
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# 🟩🟩🟩🟩🟦
# 🟩🟩🟦🟩🟦
# 🟩🟩🟦🟦🟦
# 🟦🟦🟦🟦🟦

# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
# 🟩🟩🟦🟦🟦   ← group A
# 🟩🟩🟦🟦🟦   ← group A
# 🟦🟦🟩🟦🟦   ← group B (alone)
# 🟦🟦🟦🟩🟩   ← group C


def numIsIland(grid):
    count = 0
    rows = len(grid)
    cols = len(grid[0])

    def sink(r, c):
        if r < 0 or r > rows or c < 0 or c > cols:
            return

        if grid[r][c] != "1":   # water or already sunk
            return

        grid[r][c] = "0"        # sink it

        sink(r + 1, c)          # sink it in 4 directions
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1) 

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)      # for nested function, we should keep senk function body before it is called(upper)
    return count

print(numIsIland([
   ["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","0"]
 ]))


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Max Area of Island

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:
# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    max_area = 0

    def sink(r, c):
        nonlocal count
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 

        if grid[r][c] != 1:
            return 

        grid[r][c] = 0
        count += 1

        sink(r + 1, c)
        sink(r - 1, c)
        sink(r, c + 1)
        sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count = 0
                sink(r, c)

                if count > max_area:
                    max_area = count
    return max_area                

print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))

# Or---instead of using count, return the area directly

def maxAreaOfIsland(grid):
    rows = len(grid)
    cols = len(grid[0])
    max_area = 0

    def area(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return 0

        if grid[r][c] != 1:
            return 0

        grid[r][c] = 0
        return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c + 1) + area(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                max_area = max(max_area, area(r,c))
    return max_area         
   
print(maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rotting Oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Note:
# Recursion / DFS can't model "everything at distance 1, then everything at distance 2." 
# Need level-by-level spreading — that's BFS with a queue. A queue naturally does this because it's FIFO — you finish processing everything at the current level before moving to the next.


# Stack vs Queue 

# Traversal	Data structure	Order	Behavior
# DFS	Stack (LIFO)	last in, first out	goes deep down one path
# BFS	Queue (FIFO)	first in, first out	spreads level by level
# And recursion = DFS, because recursion secretly uses the computer's call stack. That's why recursive flood fill goes deep.

# Can you use a stack here? No. LIFO would grab the most recently added orange, diving deep into one direction — so you couldn't tell which minute an orange belongs to. You need FIFO to finish all of minute 1 before starting minute 2. Your original instinct was right.

# My Q/A:

# My correct insight:
# "In that updated level I need all oranges, and order doesn't matter." [my correct understanding]

# Correct! Within a single minute, the order doesn't matter at all. Processing (1,0) before (0,1) or vice versa gives the same result.

# Where the confusion is:
# "I need the updated level just pushed, not the previous level."--[my vague understanding]

# Here's the thing: the previous level is already gone. You popped every one of them while processing that minute. They're not sitting in the queue waiting to be skipped.

# So you never need to "reach past" old ones — they've been removed.

# Watch the queue contents in a real trace
# grid = [[2,1,1],[1,1,0],[0,1,1]]

# Start of minute	Queue contains	Action	Queue after
# Minute 1	[(0,0)] ← level 0	pop (0,0), add its 2 neighbors	[(1,0),(0,1)]
# Minute 2	[(1,0),(0,1)] ← only level 1!	pop both, add their neighbors	[(1,1),(0,2)]
# Minute 3	[(1,1),(0,2)] ← only level 2!	pop both, add neighbors	[(2,1)]
# Minute 4	[(2,1)] ← only level 3!	pop it, add neighbor	[(2,2)]
# Notice: at the start of every minute, the queue holds exactly that minute's oranges — nothing older. Because each minute's oranges get popped out during their own minute.

# From Example 1:
# Minute 1: queue = [(0,0)],  size = 1
#   pop(0) → (0,0), adds (1,0) and (0,1)
#   queue = [(1,0), (0,1)]

# Minute 2: size = 2
#   pop(0) → (1,0)   
#           adds (0,2)  → queue = [(0,1), (0,2)]
#   pop(0) → (0,1)  
#           adds (2,0)  → queue = [(0,2), (2,0)]
#          This way at first level 1 finished and now level 2 start and continues...pop(0) here, 0 matters which drive to FIFO and lead to complete one by one level serially.

# That's why size = len(queue) works: it measures "how many are in the current level", and everything appended during the loop lands behind them, waiting for next minute.

# So why FIFO specifically?
# Since order within a level doesn't matter, what does FIFO actually buy you? Level separation.

# With a QUEUE (FIFO):


# queue: [level-1 oranges] then [level-2 oranges appended behind]
#         ↑ popped first          ↑ popped only after level 1 is done


def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    fresh = 0

    # find all rotten oranges + count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r,c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return     # output will be same to the input

    minutes = 0

    while len(queue) > 0 and fresh > 0:
        for i in range(len(queue)):
            r, c = queue.pop(0)  
            
# From Example 1:
# Minute 1: queue = [(0,0)],  size = 1
#   pop(0) → (0,0), adds (1,0) and (0,1)
#   queue = [(1,0), (0,1)]

# Minute 2: size = 2
#   pop(0) → (1,0)   
#           adds (0,2)  → queue = [(0,1), (0,2)]
#   pop(0) → (0,1)  
#           adds (2,0)  → queue = [(0,2), (2,0)]
#          This way at first level 1 finished and now level 2 start and continues...pop(0) here, 0 matters which drive to FIFO and lead to complete one by one level serially.
   

        # Rotting all the adjacents
            # Down
            if r + 1 < rows and grid[r+1][c] == 1:
                grid[r + 1][c] = 2
                fresh -= 1
                queue.append((r+1, c))

            # Up
            if r - 1 >= 0 and grid[r-1][c] == 1:
                grid[r-1][c] = 2
                fresh -= 1
                queue.appen((r-1, c))

            # Right
            if c + 1 < cols and grid[r][c+1] == 1:
                grid[r][c+1] = 2
                fresh -= 1
                queue.append((r, c+1))

            # Left
            if c - 1 >= 0 and grid[r][c-1] == 1:
                grid[r][c-1] = 2
                fresh -= 1
                queue.append((r, c-1))

        # after rotting all the adjacents(completion of one level) then increase minute
        minutes += 1        

    
    if fresh == 0:
        return minutes
    # handling example 2
    else:
        return -1

print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))