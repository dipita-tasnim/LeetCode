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
    
