# Longest Palindromic substring

# Given a string s, return the longest palindromic substring in s.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Note:
# Sliding window needs a rule where "invalid" reliably means "shrink."
# For palindromes, "invalid right now" doesn't mean shrink — it might mean grow more. So there's no reliable rule, and sliding window can't be used.

# Ex. "abaxaba"

# window "aba"    → IS a palindrome 
# add next char → "abax" → NOT a palindrome 
# Now what? Sliding window logic says "invalid → shrink from the left." So you'd shrink "abax" → "bax" → "ax"...

# But the actual longest palindrome is "abaxaba" — the whole thing!


# The right approach: Expand From Center
# "Center" means the center of the palindrome we're currently testing, not the center of given s.

def longestPalindrome(s):
    result = ""

    def expand(left, right):
        while left >=0 and right < len(s) and s[left]== s[right]:
            left -= 1       # shifting from the middle
            right += 1
        return s[left + 1 : right]  # slicing

    for i in range(len(s)):
        odd = expand(i, i)      # resulted string increasing gradually. once we get odd, then other time we get even..continue
        even = expand(i, i + 1)

        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    return result

print(longestPalindrome("babad"))

# why returning left + 1?
# left=-1, right=3 → left < 0 → STOP 
# Now left = -1 and right = 3

# In Python slicing s[a:b], the end b is EXCLUSIVE (it stops before b)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Encode and Decode Strings

# Problem:
# Design an algorithm to encode a list of strings into a single string. The encoded string is then decoded back to the original list of strings.
# You need to implement two functions:
# encode(strs) → takes a list of strings, returns a single string
# decode(s) → takes that single string, returns the original list of strings

# Example 1:
# Input:  ["hello", "world"]
# Output: ["hello", "world"]
# encode(["hello","world"]) → some single string
# decode(that string)       → ["hello", "world"]

# Example 2:
# Input:  [""]          (a list with one empty string)
# Output: [""]

# The catch: the strings can contain any characters — including spaces, commas, or whatever separator you might think of using. So you can't just join with a comma.

# Approach:

# The challenge — why it's tricky
# Your first instinct might be: "join with a comma!"

# "hello,world"   # then split by comma
# But what if a string itself contains a comma? Like ["a,b", "c"] → "a,b,c" → decoding by comma gives ["a", "b", "c"] — wrong! You can't tell the real commas from the separator.

# No single character is safe as a separator, because any character could appear inside the strings.

# The clever solution: length-prefixing
# Instead of a separator, store each string's length before it, with a marker:

# Format for each string:   <length>#<string>
# For ["hello", "world"]:

# "5#hello5#world"
# 5# → "the next 5 characters are one string"
# read 5 chars → "hello"
# 5# → next 5 chars
# read 5 chars → "world"
# Why this works: the length tells you exactly how many characters to read, so it doesn't matter if the string contains #, commas, or anything else.

def encode(string_arr):
    result = ""
    for i in string_arr:
        result += str(len(i)) + "#" + i
    return result

def decode(s):
    original = []
    i = 0
    while i < len(s):
        # read the length (digits before '#')
        j = i
        while s[j] != "#":
            j += 1              # '#' could be included here in every last iteration of each chunk. thats why we need 'start'.
        length = int(s[i : j])  # the number before '#'

        # read exactly length chars after the '#'
        word_start = j + 1
        word = s[word_start : word_start + length]
        original.append(word)

        # move to the next chunk
        i = word_start + length
    return original

encoded = encode(["hello", "world"])
print(encoded)          # 5#hello5#world
print(decode(encoded))  # ['hello', 'world'] 

# or----no need j in the decode part

def decode(s):
    result = []
    i = 0
    while i < len(s):
        # STEP 1: find the '#' that ends the number
        hash_pos = s.index("#", i)          # position of next '#' from i
        length = int(s[i:hash_pos])         # the number before it

        # STEP 2: grab `length` chars after the '#'
        word_start = hash_pos + 1
        word = s[word_start : word_start + length]
        result.append(word)

        # move past this whole chunk
        i = word_start + length
    return result

    

# Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# idea:
# answer[i] = (product of everything before i) × (product of everything after i)
# That's exactly what this does. Nothing different conceptually. The only "trick" is how it computes the before/after products efficiently.

# left starts at 1
# i=0: left = 1
# i=1: left = 1        (= product before index 1 = just nums[0]=1)
# i=2: left = 2        (= product before index 2 = nums[0]×nums[1] = 1×2)
# i=3: left = 6        (= product before index 3 = 1×2×3)
# Notice: left doesn't recompute from scratch each time. It just multiplies the previous left by one more number:

# left = left * nums[i]    # yesterday's product × today's number
# That's the whole "magic" — each step builds on the last one. Instead of recalculating "everything before i" from the beginning every time (which would be slow, O(n²)), it remembers the running product and extends it by one. 
# So answer[i] = before[i] × after[i] — your original idea, computed cleverly.

def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    # left products
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]     # after loop ends: answer = [1, 1, 2, 6]

    # right products   
    right = 1
    for i in range(n-1, -1, -1):
        answer[i] = answer[i] * right  # combine with left product(comment part)
        right *= nums[i]    # after loop ends: answer = [24, 12, 8, 6]

    return answer 
 
print(productExceptSelf([-1,1,0,-3,3]))  


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Clone Graph

# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }
 
# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: There are 4 nodes in the graph.
# 1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
# 3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
# 4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

# Example 3:
# Input: adjList = []
# Output: []
# Explanation: This an empty graph, it does not have any nodes.


# Note - explanation of code: 

# dfs(4)(from neighbor loop) → return clone4
# dfs(3)(") → return clone3
# dfs(2)(") → return clone2
# dfs(1)(") → return clone1
# Each return clone hands one node's clone back to whoever called that dfs (its parent in the recursion). These are internal hand-offs between recursive calls — not the final answer.

# return dfs(node) — returns ONCE (the final answer)
# This line runs once, in the outer function. It receives the result of dfs(clone1) — and passes it out as the final answer. 
# returning just clone 1 as the final answer(clone 1 ultimately connected to all- we get full graph eventually- leetcode will make them as a list- my task is just return a node)

#------------------------------
# Node class - given by leetcode
# class Node:
#     def__init__(self, val):
#         self.val = val
#         self.neighbors = []
#-------------------------------

def cloneGraph(node):
    if not node:       # empty graph - nothing to clone
        return None
    
    old_to_new = {}    # original_node:{its clone} 

    def dfs(node):
        if node in old_to_new:
            return old_to_new[node]

        clone = Node(node.val)  # make a new node with the same value
        old_to_new[node] = clone      # save/ store it before touching neighbor

        for neighbor in node.neighbors:           # for each neighbor to the original
            clone.neighbors.append(dfs(neighbor)) # clone it, attach to clone's neighbor list
        return clone    # this node is fully cloned, return it
    
    return dfs(node)    # start cloning at first node, return the final result.


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Number of Provinces

# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.

# Example 1:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

# Example 2:
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3

# Trace

# city 1: not visited → count = 1, visit 1
#     dfs(1): row 1 = [1,1,0]
#         city 2 is connected & unvisited → visit 2, dfs(2)
#             dfs(2): row 2 = [1,1,0] → city1 visited, city2 visited → nothing new
#     → province {1, 2} done

# city 2: already visited → skip

# city 3: not visited → count = 2, visit 3
#     dfs(3): row 3 = [0,0,1] → only itself → nothing new
#     → province {3} done

# count = 2 
# Cities 1 and 2 form one province; city 3 is alone → 2 provinces.

# Example 2: [[1,0,0],[0,1,0],[0,0,1]]

#        city1 city2 city3
# city1 [  1     0     0  ]   → connects only to itself
# city2 [  0     1     0  ]   → connects only to itself
# city3 [  0     0     1  ]   → connects only to itself

# city 1: not visited → count = 1, visit 1
#     dfs(1): row = [1,0,0] → only itself → nothing new
# city 2: not visited → count = 2, visit 2
#     dfs(2): row = [0,1,0] → only itself → nothing new
# city 3: not visited → count = 3, visit 3
#     dfs(3): row = [0,0,1] → only itself → nothing new

# count = 3 
# No city connects to another → each is its own province → 3.

# One thing to keep clear 
# Whether you call them city 1,2,3 or city 0,1,2, the code uses matrix indices 0,1,2:


# for city in range(n):        # city = 0, 1, 2 (indices)
#     if isConnected[city][neighbor] == 1:
# The "city 1, 2, 3" naming is just for human reading — internally it's always 0-indexed (row 0 = first city). So isConnected[0] is the first city's row, no matter what you call it.


# this problem is nxn squared matrix - row, col number same => n = len(input)

def findCircleNum(isConnected):
    n = len(isConnected)
    visited = set()
    count = 0

    def dfs(city):
        for neighbor in range(n):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)   # mark as connected city
                dfs(neighbor)           # visit its connection too


    for city in range(n):
        if city not in visited:
            count += 1
            visited.add(city)
            dfs(city)       # visit the whole province
    return count             