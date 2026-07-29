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