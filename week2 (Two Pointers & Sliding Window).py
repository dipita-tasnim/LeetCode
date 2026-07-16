# Two Sum II - Input Array is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers index1 and index2, each incremented by one, as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


def two_sum_sorted(numbers, target):
    seen = {}
    result = []
    for i in range(len(numbers)):
        complement = target - numbers[i]
        if complement in seen:
             result.append(seen[complement]+1)
             result.append(i+1)
             return result
        else:
            seen[numbers[i]] = i     
print(two_sum_sorted([2,3,4], 6))            

# or---since this is sorted, so, two pointer technique will work

def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total < target:  # important
            left += 1
        elif total > target:
            right -= 1    

print(two_sum_sorted([2,3,4], 6)) 

#---------------------------------------------------------------------------------------------------------------------------------------------

# Move Zeros

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# Output: [0]

def move_zeros(nums):  # for handling two consequetive zeros- need slow, fast pointer to swap with.
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        fast += 1    
    return nums   
print(move_zeros([0,1,0,3,12]))

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

# Example 2:
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.

# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.   


# for not considering duplicate triplets, we will use set as set by default keeps only unique touples.
# 3Sum needed 2 loops(nested-1 outer). similarly if 4Sum- 3 loops(nested- 2 outer)
# at first sorting so that we can use two pointer (efficient approach- faster)

def three_sum(nums):
    nums.sort()
    result = set()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.add((nums[i], nums[left], nums[right])) # touple

                left += 1
                right -= 1

            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            else:
                right -= 1

    final = []
    for i in result:
        final.append(list(i))
    return final

print(three_sum([-1,0,1,2,-1,-4]))                    


#------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Logic Note: max area will come combination of height and width both, not only with max two heights. such area that water should not overload and keep as much high as it can be kept, width should be maximized.
# Here, we will use two pointer. Two pointer is not only for sorted array. it is used in case such that we can safely eliminate one end each step.

def max_area(height):
    left = 0
    right = len(height) - 1
    best = 0

    while left < right:
        h = min(height[left], height[right]) # shorter line limits the water
        w = right - left                     # width between them
        area = h * w
        if area > best:
            best = area

        if height[left] < height[right]:     # move the shorter line inward
            left += 1
        else:
            right -= 1
    return best              
  
print(max_area([1,8,6,2,5,4,8,3,7]))   # 49
print(max_area([1,1]))                  # 1
print(max_area([1,2,1]))                # 2

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Sliding window technique - left and right both move right: window grows and shrinks

def longest_substring(s):
    left = 0
    unique_sub = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in unique_sub: 
            unique_sub.remove(s[left])
            left += 1             # moving forward: window shrinks
        unique_sub.add(s[right])  # moving forward: window grows

        if len(unique_sub) > max_len:
            max_len = len(unique_sub)
    return max_len        

print(longest_substring("pwwkew"))    


# Brut force
def longest_substring(s):
    max_len = 0
    for i in range(len(s)):          # try every starting point
        seen = set()   # Resets
        for j in range(i, len(s)):   # extend until you hit a repeat
            if s[j] in seen:
                break                 # duplicate → stop, try next start
            seen.add(s[j])
            if len(seen) > max_len:
                max_len = len(seen)
    return max_len

# A nested loop is only O(n²) if the inner loop RESTARTS each time. If the inner pointer only moves forward and never resets, the total work across all iterations is still just O(n) — even though it looks nested.

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Longest Repeating Character Replacement

# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


# Hints:
# cost ≤ k (valid)	I can make this window uniform within budget	Grow → move right forward (try a bigger window)
# cost > k (invalid)	Too many replacements needed, over budget	Shrink → move left forward (make window smaller)
# That's the entire basis. Grow while affordable, shrink when not.

# Why grow when valid?
# If the current window is affordable, maybe an even bigger one is too. So you push right forward to test a larger window — you're greedily trying to find the longest possible.

# Why shrink when invalid?
# If the window costs more than k, it's impossible to make uniform. So you drop a character from the left to reduce the cost back under budget.
# for eaxmple, suppose in step/loop 5: cost = k = (window_len - max_freq) = (5 - 3)=2[k=1]. then (6 - 3[no max char found in the next])=3
# (6 - 2[max char found in the next])=4>k [all is invalid as greater than k and no chance to less or equal to k unless we shrink]

def character_replacement(s, k):

    left = 0
    max_len = 0
    count = {}


    for right in range(len(s)):
        if s[right] in count:
            count[s[right]] += 1
        else:
            count[s[right]] = 1  

        max_freq = max(count.values())  

        window_len = right - left + 1
        cost = window_len - max_freq

        while cost > k:
            count[s[left]] -= 1
            left += 1
            window_len = right - left + 1
            cost = window_len - max_freq
            max_freq = max(count.values())

        if window_len > max_len:
            max_len = window_len
    return max_len      

print(character_replacement("AABABBA", 1))

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# IS Subsequence

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:
# Input: s = "abc", t = "ahbgdc"
# Output: true

# Example 2:
# Input: s = "axc", t = "ahbgdc"
# Output: false

# Two Pointer Problem but both ponters moving forward (not inward) - new variation of two pointer
# Not using sliding window because this is not substring (a contiguous case), that's why. window is for contiguous.

def isSubsequence(s, t):

    pointer_s = 0
    pointer_t = 0

    while pointer_s < len(s) and pointer_t < len(t):
        if s[pointer_s] == t [pointer_t]:
            pointer_s += 1
        pointer_t += 1

    if pointer_s == len(s):
        return True
    else:
        return False   
    
print(isSubsequence("abc","ahbgdc"))

#-------------------------------------------------------------------------------------------------------------------------------------------

#  Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.
# The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
             

def remove_duplicate(nums):
    index = 1    # first element is always unique

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[index] = nums[i]
            index += 1

    return index

print(remove_duplicate([1,1,2]))