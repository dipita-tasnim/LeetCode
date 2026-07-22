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