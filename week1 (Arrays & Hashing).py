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

#------------------------------------------------------------------------------------------------------------------------------------------

# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Example 2:
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# O(1) --1 array--in place change

def reverse_string(arr):
    left = 0
    right = len(arr)-1

    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp

        left += 1
        right -= 1
    return arr 

print(reverse_string(["h","e","l","l","o"]))  

# or--O(n) ---created a new array makes 2 array--extra n space

def reverse_string(arr):
    reverse_arr = []
    for i in range(len(arr)-1,-1,-1):
        reverse_arr.append(arr[i])
    return reverse_arr

print(reverse_string(["h","e","l","l","o"]))

#------------------------------------------------------------------------------------------------------------------------------------------------

# Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

def merge_sorted_array(nums1, m, nums2, n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    return nums1    

print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))


# or---3 pointer (for learning purpose)

def merge_sorted_array(nums1, m, nums2, n):
    p1 = m - 1      # last position in real nums1
    p2 = n - 1      # last position in nums2
    p = m + n - 1   # last position in resulted nums1

    while p2 >= 0: # while nums2 still has element
        if p1 >= 0 and nums1[p1] > nums2[p2]: 
            nums1[p] = nums1[p1]   # bigger one should be at towards the last
            p1 -= 1                # decreasing the last position, going towards left
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    return nums1    
print(merge_sorted_array([1,2,3,0,0,0], 3, [2,5,6], 3))   

#----------------------------------------------------------------------------------------------------------------------------------------

# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Explanation:
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

def group_anagrams(arr):
    sorted_arr = []
    output_arr = []
    seen = {}
   
    for string in arr:
        s = sorted(string)             # use 'sorted' not 'sort'. 'sort' is only for array. 'sorted' works for string/arr/anything
        glue_sorted = "".join(s)
        #sorted_arr.append(glue_sorted) # sorted_arr = ["aet", "aet", "ant", "aet", "ant", "abt"]

        if glue_sorted in seen:
            seen[glue_sorted].append(string)
        else:
            seen[glue_sorted] = [string]    

    for i in seen.values():
        output_arr.append(i)
    return output_arr
    
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Majority Element

# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

def majority_element(arr):
    count = {}
    for i in arr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for key in count:
        if count[key] > len(arr)//2:
            return key          

print(majority_element([3,2,3]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# Concatenation of Array

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays.
# Return the array ans.

# Example 1:
# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]

# Example 2:
# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]

def concate_array(arr):
    ans = []
    for i in arr:
        ans.append(i)
    for i in arr:
        ans.append(i)
    return ans
print(concate_array([1, 2, 1]))        

# or ---in one loop
# Note: two individual loops (not nested) and just one single loop cover same complexity. So, either one process can be used. 

def concate_array(arr):
    ans = [0] * (2* len(arr))
    index = 0
    idx = 0
    for i in range(len(ans)):
        if i < len(arr):
            ans[index] = (arr[i])
            index += 1
        else:
            ans[index] = (ans[idx])
            index += 1
            idx += 1    
    return ans
print(concate_array([1,2,1]))        

# Or (simpler)

def concate_array(arr):
    n = len(arr)
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = arr[i]      # first half
        ans[i + n] = arr[i]  # second half
    return ans
print(concate_array([1,2,1]))   

#---------------------------------------------------------------------------------------------------------------------------------------------------------------

# Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def remove_element(arr, val):
    index = 0
    for i in range(len(arr)):
        if arr[i] != val:
            arr[index] = arr[i]
            index += 1
    return index, arr        
print(remove_element([0,1,2,2,3,0,4,2], 2))        

# two-pointer approach overwrites the front with kept elements but never touches the tail. So old values (including 2's) stay behind at the end — untouched but harmless:
# only the first k elements matter
# Your output is (5, [0, 1, 3, 0, 4, 0, 4, 2]).

# k = 5
# The first 5 elements are [0, 1, 3, 0, 4] → all non-2 
# The rest — [0, 4, 2] at positions 5, 6, 7 — are leftover garbage that doesn't matter. Those are the "underscores" from the problem


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Squares of a Sorted Array

# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2:
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

def squared_sorted(nums):

    squared = []
    for i in nums:
        squared.append(i**2)
    
    squared.sort()
    return squared

print(squared_sorted([-4,-1,0,3,10]))

# Or--two pointer sorting (faster)

def squared_sorted(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    idx = n - 1

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[idx] = left_square
            left += 1
        else:
            result[idx] = right_square
            right -= 1
        idx -= 1
    return result        

print(squared_sorted([-4,-1,0,3,10]))

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

# Example 3:
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

def plus_one(digits):
    s = ""
    res = []
    for i in digits:
        s += str(i)
    print(s) 

    plus = int(s) + 1
    plus_s = str(plus)

    for i in plus_s:
        res.append(int(i))
    return res    

print(plus_one([1, 2, 3]))


#------------------------------------------Week 1 Done--------------------------------------------------------