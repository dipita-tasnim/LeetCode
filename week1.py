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

# or One Loop--> O(n)

def duplicate(arr):
    seen = {}
    for i in arr:
        if i not in seen:
            seen[i] = 1
        else:
            seen[i] += 1

    for i in seen.values():
        if i > 1:
            return True
        else:
            return False

# or        

# Dict

def duplicate(arr):
    seen = {}
    for i in arr:
        if i in seen:
            return True
        else:
            seen[i] = 1
    return False 

# set

def duplicate(arr):
    seen = set()
    for i in arr:
        if i in seen:
            return True
        else:
            seen.add(i)
    return False

# list --O(n^2)

def duplicate(arr):
    seen = []
    for i in arr:
        if i in seen:
            return True  
        else:
            seen.append(i)
    return False                   

       
# Note:
# List → stored in order; to find something, Python checks each item one by one → O(n). for every element → O(n) × O(n) = O(n²).
# Set / Dict → uses hashing (like an index/address system); it jumps straight to where the item would be → O(1), no scanning.
# That's the whole reason this topic is called "Arrays & Hashing" — sets and dicts are the "hashing" tools that make lookups instant.

#-----------------------------------------------------------------------------------------------------------------------------------------------

# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise. 

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 

def is_palindrome(s):
    forward = ""
    for i in s:
        if ("a" <= i <= "z") or ("A" <= i <= "Z") or ("0" <= i <= "9"):
            forward += i.lower()

    reverse = ""
    reverse = forward[::-1]

    if forward == reverse:
        return True
    else:
        return False
    
# Or--using two pointer (instead of reversing)

def is_palindrome(s):
    forward = ""
    for i in s:
        if ("a" <= i <= "z") or ("A" <= i <= "Z") or ("0" <= i <= "9"):
            forward += i.lower()

    left = 0
    right = len(forward) - 1

    while left < right:
        if forward[left] != forward[right]:
            return False
        left += 1
        right -= 1
    return True

#---------------------------------------------------------------------------------------------------------

# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

def profit(arr):
    min_price = arr[0]
    max_profit = 0

    for price in arr:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = (price - min_price)      
    return max_profit   
