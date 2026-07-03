# Two Sum

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
                
print(twoSum([2,7,11,15], 9))

# or One Loop--> O(n)

def twoSum(arr, target):
    seen = {} # seen has {value:index}
    for i in range(len(arr)):
        complement = target - arr[i]  # complement has value
        if complement in seen:
            return (seen[complement], i)
        seen[arr[i]] = i

print(twoSum([2,7,11,15], 9))


#-------------------------------------------------------------------------------------------------------------------------------------

# Valid Anagram

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

def anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    elif sorted(string1) == sorted(string2):
        return True
    else:
        return False
print(anagram('anagram', 'nagaram'))

# or One Loop--> O(n)

def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    count1 = {}
    for i in s1:
        if i in count1:
            count1[i] = count1[i] + 1
        else:
            count1[i] = 1

    count2 = {}
    for i in s2:
        if i in count2:
            count2[i] = count2[i] + 1
        else:
            count2[i] = 1

    if count1 == count2:
        return True
    else:
        return False                       

#------------------------------------------------------------------------------------------------------------------

# Contains Duplicate

# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true
# Explanation:
# The element 1 occurs at the indices 0 and 3.

# Example 2:
# Input: nums = [1,2,3,4]
# Output: false

def duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False    
print(duplicate([1,2,3,1]))